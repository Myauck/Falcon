import cv2

class Camera: 
    
    __capture: cv2.VideoCapture
    __detect: bool

    def __init__(self, capture: cv2.VideoCapture):
        self.__capture = capture
        self.__detect = False

    def setCapture(self, capture: bool):
        self.__detect = capture

    def isCaptured(self):
        return self.__detect

    def getCapture(self): 
        while self.__detect:
            _, img = self.__capture.read()
            # Detecte les visages
            cv2.imshow('img', img)
            # arreter si l'on appuie sur echap
            k = cv2.waitKey(30) & 0xff
            if k==27:
                self.__detect=False
        self.__capture.release()