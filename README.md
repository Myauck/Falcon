# Falcon

## Présentation

### Description du projet

**Drone de surveillance équipée d'un système de prise de vue**.

Le project consiste à programmer un drône de surveillance équipé d'un système de prise de vue.

L'objectif est de programer le pilotage du drone en wifi avec une interface cliente, une interface graphique pour récupérer les informations de télémétrie du drône, et une fonctionnalité qui permet de récupérer et de traîter les images enregistrées par le drône.

### Tâches à réaliser

Les *Difficultés* sont approximatives

- [ ] Configurer la liaison wifi du drône *(Difficulté 1/5)*
- [ ] Installer et configurer les services web sur le PC embarqué *(Difficulté 1/5)*
- [ ] Créer un site web pour entrer un parcours géo-localisé *(Difficulté 3/5)*
- [ ] Créer une base de données pour stocker les données du parcours *(Difficulté 3/5)*
- [ ] Programmer l'ajout d'un parcours dans la base de données *(Difficulté 4/5)*
- [ ] Créer une interface graphique avec la bibliothèque Tkinter *(Difficulté 1/5)*
- [ ] Récupérer les informations de télémétrie du drône *(Difficulté 3/5)*
- [ ] Afficher les données et l'image émise par le drone dans l'interface *(Difficulté 3/5)*
- [ ] Afficher le visage détecté *(Difficulté 4/5)*
- [ ] Configurer la caméra embarquée du drône *(Difficulté 2/5)*
- [ ] Installer les bibliothèques de traitement d'images OpenCV *(Difficulté 2/5)*
- [ ] Programmer un traitement d'images pour détecter un visage *(Difficulté 4/5)*
- [ ] Stocker l'image du visage dans une base de données *(Difficulté 4/5)*

## Installation

### Modules et dépendances

#### Connexion au Drone

- **Wheel**
- **PyMavlink**
- **[Dronekit](https://github.com/dronekit/dronekit-python)**

```bash
$: python3 -m pip install wheel pymavlink dronekit
```

#### Passage par interface web

- **SimpleJSON**
- **PID**
- **CherryPy**
- **Jinja2**
- **DroneKit**
- **DroneKit-sitl**

```bash
$: python3 -m pip install simplejson pid cherrypy jinja2 dronekit dronekit-sitl
```

## Informations complémentaires

- SimpleJSON permet de traîter les ficher et de les éditer comme un dictionnaire en Python
- CherryPy est un module basé sur l'application WEB qui permet d'afficher une map indiquant plusieurs caractéristiques intéressantes
- *Delivery.py*
  - Class Drone:
  - \+ index
  - \+ track (coordonnées) (route : /track)
  - \+ command (instructions) (route : /command)
  - \+ get_template (rendu View) (rout : *FICHER*.html)