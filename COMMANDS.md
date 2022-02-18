# Falcon Tello Commands

Il y a plusieurs commandes qui permettent d'effectuer différentes actions. Ces commandes sont enregistrées par défaut dans l'API du drone. Selon les commandes qu'on entrera, le drone enverra une réponse ou non.

:information_source: Informations :

Les commandes qui **effectueront les mouvements** seront nommées les **commandes de contrôles**

Les commandes qui **modifieront les valeurs** seront les nommées les **commandes de configuration**

Les commandes qui **renverrons des valeurs** seront nommées les **commandes de récupérations**

**Version de l'API: 1.1.6**

## Les commandes de contrôle

- `takeoff` : Décollage automatique (hauteur de 1 mètre environ)
- `land` : Atterissage automatique
- `streamon` : Permet d'activer le flux vidéo du drone à l'aide d'une caméra intégrée
- `streamoff` : Désactive le flux vidéo du drone
- `emergency` : Ordonne au drone d'arrêter la rotation du moteur
- `up <y>` : Vol vers le haut en fonction de *y* (entre y=20 et y=500) (exprimée en *centimètres cm*)
- `down <y>` : Vol vers le bas en fonction de *y* (entre y=20 et y=500) (exprimée en *centimètres cm*)
- `left <x>` : Vol vers la gauche en fonction de *x* (entre x=20 et x=500) (exprimée en *centimètres cm*)
- `right <x>` : Vol vers la droite en fonction de *x* (entre x=20 et x=500) (exprimée en *centimètres cm*) 
- `forward <z>` : Vol vers l'avant du drone en fonction de *z* (entre z=20 et z=500) (exprimée en *centimètres cm*) 
- `backward <z>` : Vol vers l'arrière du drone en fonction de *z* (entre z=20 et z=500) (exprimée en *centimètres cm*) 
- `cw <angle>` : Rotation du drone dans le sens des aiguilles en fonction de l'angle *angle* (entre 1 et 360) (exprimée en *degré °*)
- `cww <angle>` : Rotation du drone dans le sens inverse des aiguilles en fonction de l'angle *angle* (entre 1 et 360) (exprimée en *degré °*)
- `flip` : \*EN COURS\*
- `go <x> <y> <z> <speed>` : Faire déplacer le drone vers les coordonnées (*x*;*y*;*z*) à une vitesse *speed* (exprimée en *centimètres par secondes cm/s*)
- `stop` : Arrête tout mouvement du drone et se met automatiquement en mode survol
- `curve` : \*EN COURS\*
- `jump` :  \*EN COURS\*

## Les commandes de configuration

- `speed <speed>` : \*EN COURS\*
- `rc <a> <b> <c> <d>` : \*EN COURS\*
- `wifi <ssid> <password>` : \*EN COURS\*
- `mon` : \*EN COURS\*
- `moff` : \*EN COURS\*
- `mdirection <mdir>` : \*EN COURS\*
- `ap <ssid> <password>` : \*EN COURS\*
 
## Les commandes de récupération

- `speed?` : Récupère la vitesse actuelle du drone (entre 10 et 100) (exprimée en *centimètre par seconde cm/s*)
- `battery?` : Récupère le pourcentage de batterie du drone (entre 10 et 100) (exprimée en *pourcentages %*)
- `time?` : Récupère le temps de fonctionnement du moteur (exprimée en *secondes*)
- `wifi?` : Récupère le rapport de la qualité et le bruit du signal du réseau du drone
- `sdk?` : Obtient le numéro SDK du drone
- `sn?` : Obtient le numéro de série du drone
- `height?` : Récupère la hauteur du drone
- `temp?` : Récupère la températeur grâce à un capteur intégré
- `attitude?` : Récupère l'attitude du drone grâce à un capteur intégré
- `baro?` : Récupère la pression atmosphérique grâce à un capteur intégré
- `acceleration?` : \*EN COURS\*
- `tof?` : \*EN COURS\*


