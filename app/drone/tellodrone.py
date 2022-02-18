import os
import socket
import queue
import threading
import time
import datetime

import cv2
import numpy as np
import paddlehub as hub
from PIL import Image

from tello.stats import Stats
from tello.frame2html import VideoCamera, run_app

q = queue.Queue()

# q.queue.clear()


class TelloDrone:

    def __init__(self, local_ip: str = '', local_port: int = 8889, te_ip: str = '192.168.10.1',
        te_port: int = 8889, debug: bool = True):

        # Ouvrir le port local 8889 en UDP pour effectuer la communication avec le drone 
        self.local_ip = local_ip
        self.local_port = local_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.local_ip, self.local_port))

        # Définir l'adresse IP et les informations de port du drone
        self.te_ip = te_ip
        self.te_port = te_port
        self.te_address = (self.te_ip, self.te_port)
        self.log = []
        self.picture_path = ''
        self.file_path = ''
        self.frame = None

        # Charger le modèle de reconnaissance animal
        self.module = hub.Module(name="resnet50_vd_animals")

        # Initialisation du thread de réponse du drone
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        # Options d'exécution du projet
        self.stream_state = False
        self.camera_state = False
        self.color_state = False
        self.video_state = False
        self.save_state = False
        self.picture_state = False
        self.animal_state = False
        self.flip_frame = False
        self.now_color = 0
        self.MAX_TIME_OUT = 15.0
        self.debug = debug

        # Régler le drone en mode commande
        self.command()

    def send_command(self, command: str, query: bool = False):
        # Créer une nouvelle entrée de log pour la réponse de commande
        self.log.append(Stats(command, len(self.log)))

        # Envoi de commandes aux drones
        self.socket.sendto(command.encode('utf-8'), self.te_address)
        # Affichage du message de confirmation (debug)
        if self.debug is True:
            print('Send Command: {}'.format(command))

        # Vérifier si la commande a expiré (en fonction de la valeur de MAX_TIME_OUT)
        start = time.time()
        while not self.log[-1].got_response():  # Exécution sans réponses reçue dans le fichier log
            now = time.time()
            difference = now - start
            if difference > self.MAX_TIME_OUT:
                print('Connect Time Out!')
                break

        # Afficher la réponse du drone
        if self.debug is True and query is False:
            print('Response: {}'.format(self.log[-1].get_response()))

    def _receive_thread(self):
        while True:
            # Vérifier la réponse du drone, lever une erreur de socket dans le cas différent
            try:
                self.response, ip = self.socket.recvfrom(1024)
                self.log[-1].add_response(self.response)
            except socket.error as exc:
                print('Error: {}'.format(exc))

    def _cap_video_thread(self):
        # Création d'objets de capture de flux vidéo
        cap = cv2.VideoCapture('udp://' + self.te_ip + ':11111')
        # cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        while self.stream_state:
            ret, frame = cap.read()
            while ret:
                ret, frame = cap.read()
                if self.flip_frame:
                    frame = cv2.flip(frame, 0)
                cv2.imshow("DJI Tello", frame)
                q.put(frame)
                k = cv2.waitKey(1) & 0xFF
                # Si la touche 'Esc' est appuyée, le flux vidéo est désactivé
                if k == 27:
                    break
        cap.release()
        cv2.destroyAllWindows()

    def _service_video_thread(self):
        while True:
            self.frame = q.get()
            # k = cv2.waitKey(1) & 0xFF
            # Si la touche F1 est pressée, capture d'écran de la position actuelle
            # if k == 0 or self.camera_state:
            if self.camera_state:
                self.file_path = self.picture_path + '\\' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + '.png'
                print('Chemin de l\'image enregistrée est ：', self.file_path)
                try:
                    cv2.imwrite(self.file_path, self.frame)
                except Exception as e:
                    print('L\'image n\' a pas pu être enregistrée')
                self.camera_state = False

            # Identification des animaux grâce au flux vidéo
            if self.animal_state:
                results = self.module.classification(images=[self.frame])
                # print(results)
                key_value_list = list(results[0].items())
                key_first, value_first = key_value_list[0][0], key_value_list[0][1]
                if 'non-animal' != key_first:
                    print('Le résultat du test est：', key_first, '，et est similaire à la valeur：', value_first)
                    cv2.imshow(key_first, self.frame)
                    self.animal_state = False

            # Affichage des photos
            if self.picture_state:
                file = self.file_path
                f = Image.open(file).show()
                self.picture_state = False

            # Détecter la couleur actuelle
            if self.color_state:
                self.detect_color(self.frame)
                self.color_state = False

            # Envoyer le flux vidéo vers un protocole HTTP (port 80)
            if self.video_state:
                self.video_http(self.frame)
                self.video_state = False

            # Sauvegarder le flux localement
            if self.save_state:
                self.video_save(self.frame)
                self.save_state = False

    def wait(self, delay: float):
        # Afficher les message de délai
        if self.debug is True:
            print('Wait {} Seconds...'.format(delay))

        # Les entrées dans le log sont affiché en fonction du délai
        self.log.append(Stats('wait', len(self.log)))
        # Activation du retard
        time.sleep(delay)

    @staticmethod
    def video_http(frame):
        vc = VideoCamera(frame)
        run_app()

    @staticmethod
    def video_save(frame):
        force = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', force, 20.0, (640, 480))
        frame = cv2.flip(frame, 0)
        # write the flipped frame
        out.write(frame)

    def get_log(self):
        return self.log

    def take_picture(self, path=os.getcwd()):
        """Effectuer une capture de photo"""
        self.camera_state = True
        self.picture_path = path

    def show_picture(self):
        """Afficher la capture"""
        self.picture_state = True

    def flip_video(self):
        """翻转视频，在加装下视镜片的情况下开启"""
        self.flip_frame = True

    def identify_animal(self):
        """Activer l'activation des animaux"""
        self.animal_state = True

    def identify_color(self):
        """Identifier la couleur actuelle (rouge ou vert)"""
        self.color_state = True
        time.sleep(0.5)
        return self.now_color

    # Les commandes suivantes sont fortement recommandées pour une utilisation avec le SDK officiel
    # https://www.ryzerobotics.com/cn/tello/downloads

    # Commandes de contrôle
    def command(self):
        """Entrer les commandes en mode commande SDK"""
        self.send_command('command')

    def takeoff(self):
        """Décollage automatique (distance de 1m environ)"""
        self.send_command('takeoff')

    def land(self):
        """Atterrisage automatique"""
        self.send_command('land')

    def streamon(self):
        """Ouvrir le flux vidéo"""
        self.send_command('streamon')
        self.stream_state = True

        self.cap_video_thread = threading.Thread(target=self._cap_video_thread)
        self.cap_video_thread.daemon = True
        self.cap_video_thread.start()

    def streamoff(self):
        """Désactiver le flux vidéo"""
        self.stream_state = False
        self.send_command('streamoff')

    def stream_service_on(self):
        """Activer le module complémentaire de diffusion vidéo provoquera probablement un ralentissement et une latence du flux vidéo"""
        self.service_video_thread = threading.Thread(target=self._service_video_thread)
        self.service_video_thread.daemon = True
        self.service_video_thread.start()

    def detect_color(self, frame):
        """Reconnaissance des couleurs"""
        # frame = cv2.imread("test.jpg")
        hue_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        low_red_range1 = np.array([110, 43, 0])
        high_red_range1 = np.array([180, 255, 255])
        threshold_red1 = cv2.inRange(hue_image, low_red_range1, high_red_range1)
        res_red1 = cv2.bitwise_and(frame, frame, mask=threshold_red1)

        low_red_range2 = np.array([0, 43, 0])
        high_red_range2 = np.array([10, 255, 255])
        threshold_red2 = cv2.inRange(hue_image, low_red_range2, high_red_range2)
        res_red2 = cv2.bitwise_and(frame, frame, mask=threshold_red2)

        threshold_red = threshold_red1 + threshold_red2
        res_red = res_red1 + res_red2

        low_green_range = np.array([35, 43, 46])
        high_green_range = np.array([77, 255, 255])
        threshold_green = cv2.inRange(hue_image, low_green_range, high_green_range)
        res_green = cv2.bitwise_and(frame, frame, mask=threshold_green)

        res = res_red + res_green
        if cv2.countNonZero(threshold_green) > 0.5 * np.size(threshold_green):
            self.now_color = 'green'
        elif ((cv2.countNonZero(threshold_red) > 0.5 * np.size(threshold_red)) & (
                cv2.countNonZero(threshold_red) < 0.7 * np.size(threshold_red))):
            self.now_color = 'red'
        else:
            self.now_color = 'none'
            # color = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
        return self.now_color, res

    def emergency(self):
        """Arrêt de la rotation du moteur"""
        self.send_command('emergency')

    def up(self, y: int):
        """Vol vers le haut (axe vertical) entre y=20 et y=500 (mesure en cm)"""
        self.send_command('up {}'.format(y))

    def down(self, y: int):
        """Vol vers le bas (axe vertical) entre y=20 et y=500 (mesure en cm)"""
        self.send_command('down {}'.format(y))

    def left(self, x: int):
        """Vol vers la gauche (axe horizontal) entre x=20 et x=500 (mesure en cm)"""
        self.send_command('left {}'.format(x))

    def right(self, x: int):
        """Vol vers la droite (axe horizontal) entre x=20 et x=500 (mesure en cm)"""
        self.send_command('right {}'.format(x))

    def forward(self, z: int):
        """Vol vers l'avant (axe profondeur) entre z=20 et z=500 (mesure en cm)"""
        self.send_command('forward {}'.format(z))

    def back(self, z: int):
        """Vol vers l'arrière (axe profondeur) entre z=20 et z=500 (mesure en cm)"""
        self.send_command('back {}'.format(z))

    def cw(self, angle: int):
        """Rotation de dans le sens des aiguilles d'une montre d'un angle (en °) entre 1 et 360°"""
        self.send_command('cw {}'.format(angle))

    def ccw(self, angle: int):
        """Rotation de dans le sens INVERSE des aiguilles d'une montre d'un angle (en °) entre 1 et 360°"""
        self.send_command('ccw {}'.format(angle))

    def flip(self, direction: str):
        """朝direction方向翻滚，左侧（left）缩写为l，同理right=r，forward=f，back=b"""
        self.send_command('flip {}'.format(direction))

    def go(self, x: int, y: int, z: int, speed: int):
        """Voler vers les coordonnées x, y, z, avec une vitesse fixée en cm par sec
            limites:
                x: -500 - 500
                y: -500 - 500
                z: -500 - 500
                speed: 10 - 100(cm / s)
        x, y et z ne peuvent pas être compris entre -20 et 20 en même temps"""
        self.send_command('go {} {} {} {}'.format(x, y, z, speed))

    def stop(self):
        """Arrêter le mouvement et survoler quel que soit le moment"""
        self.send_command('stop')

    def curve(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int):
        # Documentation en cours
        self.send_command('curve {} {} {} {} {} {} {}'.format(x1, y1, z1, x2, y2, z2, speed))

    def go_mid(self, x: int, y: int, z: int, speed: int, mid: str):
        # Documentation en cours
        self.send_command('go {} {} {} {} {}'.format(x, y, z, speed, mid))

    def curve_mid(self, x1: int, y1: int, z1: int, x2: int, y2: int, z2: int, speed: int, mid: str):
        # Documentation en cours
        self.send_command('curve {} {} {} {} {} {} {} {}'.format(x1, y1, z1, x2, y2, z2, speed, mid))

    def jump_mid(self, x: int, y: int, z: int, speed: int, yaw: int, mid1: str, mid2: str):
        # Documentation en cours
        self.send_command('jump {} {} {} {} {} {} {}'.format(x, y, z, speed, yaw, mid1, mid2))

    # Commandes de configuration
    def set_speed(self, speed: int):
        # Documentation en cours
        self.send_command('speed {}'.format(speed))

    def rc_control(self, a: int, b: int, c: int, d: int):
        # Documentation en cours
        self.send_command('rc {} {} {} {}'.format(a, b, c, d))

    def set_wifi(self, ssid: str, passwrd: str):
        """Changer les accès au drone en remodifiant les valeurs du ssid et du mot de passe
            ssid: Nouveau SSID du réseau
            passwrd: Nouveau mot de passe Wi-Fi
        """
        self.send_command('wifi {} {}'.format(ssid, passwrd))

    def mon(self):
        # Documentation en cours
        self.send_command('mon')

    def moff(self):
        # Documentation en cours
        self.send_command('moff')

    def mdirection(self, mdir: int):
        # Documentation en cours
        self.send_command('mdirection {}'.format(mdir))

    def ap2sta(self, ssid: str, passwrd: str):
        """Passer le drone en mode station et permet de se connecter au réseau
            ssid: SSID du réseau à se connecter
            passwrd: Mot de passe Wi-Fi
        """
        self.send_command('ap {} {}'.format(ssid, passwrd))

    # Récupération des valeurs et informations du drone et de ses capteurs
    def get_speed(self):
        """Obtenir la vitesse actuelle en cm / s, valeur exprimée entre 10 et 100"""
        self.send_command('speed?', True)
        return self.log[-1].get_response()

    def get_battery(self):
        """Obtenir le pourcentage de batterie restant, valeur exprimée entre 10 et 100"""
        self.send_command('battery?', True)
        return self.log[-1].get_response()

    def get_time(self):
        """Obtenir le temps de fonctionnement du moteur, exprimée en sec"""
        self.send_command('time?', True)
        return self.log[-1].get_response()

    def get_wifi(self):
        """Obtient le rapport de qualité du signal / bruit du réseau Wi-Fi"""
        self.send_command('wifi?', True)
        return self.log[-1].get_response()

    def get_sdk(self):
        """Obtenir le numéro de version du SDK du drone xx(>=20)"""
        self.send_command('sdk?', True)
        return self.log[-1].get_response()

    def get_sn(self):
        """Obtient le numéro de série (SN) du drone"""
        self.send_command('sn?', True)
        return self.log[-1].get_response()

    def get_height(self):
        """Obtenir la hauteur grâce au capteur"""
        self.send_command('height?', True)
        return self.log[-1].get_response()

    def get_temp(self):
        """Obtenir la température grâce au capteur"""
        self.send_command('temp?', True)
        return self.log[-1].get_response()

    def get_attitude(self):
        """Obtenir la phase de vol"""
        self.send_command('attitude?', True)
        return self.log[-1].get_response()

    def get_baro(self):
        """Obtenir la pression atmosphérique"""
        self.send_command('baro?', True)
        return self.log[-1].get_response()

    def get_acceleration(self):
        # Documentation en cours
        self.send_command('acceleration?', True)
        return self.log[-1].get_response()

    def get_tof(self):
        # Documentation en cours
        self.send_command('tof?', True)
        return self.log[-1].get_response()
