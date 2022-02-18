# Falcon

## Présentation

### Description du projet

**Version** : 0.0.1-b4

**Drone de surveillance équipée d'un système de prise de vue**.

Le project consiste à programmer un drône de surveillance équipé d'un système de prise de vue.

L'objectif est de programer le pilotage du drone en wifi avec une interface cliente, une interface graphique pour récupérer les informations de télémétrie du drône, et une fonctionnalité qui permet de récupérer et de traîter les images enregistrées par le drône.

### Tâches à réaliser

Les *Difficultés* sont approximatives

- [x] Configurer la liaison wifi du drône *(Difficulté 1/5)*
- [x] Installer et configurer les services web sur le PC embarqué *(Difficulté 1/5)*
- [ ] Créer un site web pour entrer un parcours géo-localisé *(Difficulté 3/5)*
- [ ] Créer une base de données pour stocker les données du parcours *(Difficulté 3/5)*
- [ ] Programmer l'ajout d'un parcours dans la base de données *(Difficulté 4/5)*
- [x] Créer une interface graphique avec la bibliothèque Tkinter *(Difficulté 1/5)*
- [ ] Récupérer les informations de télémétrie du drône *(Difficulté 3/5)*
- [ ] Afficher les données et l'image émise par le drone dans l'interface *(Difficulté 3/5)*
- [ ] Afficher le visage détecté *(Difficulté 4/5)*
- [ ] Configurer la caméra embarquée du drône *(Difficulté 2/5)*
- [x] Installer les bibliothèques de traitement d'images OpenCV *(Difficulté 2/5)*
- [ ] Programmer un traitement d'images pour détecter un visage *(Difficulté 4/5)*
- [ ] Stocker l'image du visage dans une base de données *(Difficulté 4/5)*

## Installation

### Modules et dépendances

| :warning: ATTENTION                       |
|:------------------------------------------|
| La version utilisée est **Python 3.9.10** |

Si vous utilisez une version ultérieure, les risques de corruption peuvent être élevés. Pour installer la bonne version de Python, veuillez vous renseigner sur [ce lien](https://www.python.org/downloads/release/python-3910/)

#### Les différentes dépendances du projet

- **tello** *(1.2)*
- **tello-python** *(1.1.6)*
- **opencv-python** *(4.5.5.62)*
- **paddlepaddle** *(2.2.2)*
- **paddlehub** *(2.2.0)*
- **flask** *(2.0.3)*
- **Jinja2** *(3.0.3)*
- **click** *(8.0.3)*
- **itsdangerous** *(2.0.1)*
- **Werkzeug** *(2.0.3)*
- **numpy** *(1.19.3)*
- **colorama** *(0.4.4)*
- **paddle2onnx** *(0.9.0)*
- **paddlenlp** *(2.2.4)*
- **filelock** *(3.6.0)*
- **pyzmq** *(22.3.0)*
- **visualdl** *(2.2.3)*
- **Pillow** *(9.0.1)*
- **easydict** *(1.9)*
- **tqdm** *(4.62.3)*
- **colorlog** *(6.6.0)*
- **rarfile** *(4.0)*
- **matplotlib** *(3.5.1)*
- **pyyaml** *(6.0)*
- **packaging** *(21.3)*
- **requests** *(2.27.1)*
- **astor** *(0.8.1)*
- **decorator** *(5.1.1)*
- **protobuf** *(3.19.4)*
- **six** *(1.16.0)*
- **MarkupSafe** *(2.0.1)*
- **onnx** *(1.9.0)*
- **jieba** *(0.42.1)*
- **h5py** *(3.6.0)*
- **seqeval** *(1.2.2)*
- **multiprocess** *(0.70.12.2)*
- **idna** *(3.3)*
- **urllib3** *(1.26.8)*
- **charset-normalizer** *(2.0.12)*
- **certifi** *(2021.10.8)*
- **pandas** *(1.4.1)*
- **bce-python-sdk** *(0.8.64)*
- **flake8** *(4.0.1)*
- **Flask-Babel** *(2.0.0)*
- **shellcheck-py** *(0.8.0.4)*
- **pre-commit** *(2.17.0)*
- **kiwisolver** *(1.3.2)*
- **pyparsing** *(3.0.7)*
- **cycler** *(0.11.0)*
- **fonttools** *(4.29.1)*
- **python-dateutil** *(2.8.2)*
- **pyflakes** *(2.4.0)*
- **mccabe** *(0.6.1)*
- **pycodestyle** *(2.8.0)*
- **Babel** *(2.9.1)*
- **pytz** *(2021.3)*
- **typing-extensions** *(4.1.1)*
- **pycryptodome** *(3.14.1)*
- **future** *(0.18.2)*
- **dill** *(0.3.4)*
- **identify** *(2.4.10)*
- **cfgv** *(3.3.1)*
- **virtualenv** *(20.13.1)*
- **toml** *(0.10.2)*
- **nodeenv** *(1.6.0)*
- **scikit-learn** *(1.0.2)*
- **joblib** *(1.1.0)*
- **threadpoolctl** *(3.1.0)*
- **scipy** *(1.8.0)*
- **platformdirs** *(2.5.0)*
- **distlib** *(0.3.4)*

Voici la commande pour installer les dépendances ci-dessus:

#### Installation sur Windows 

```bash
python -m pip install tello tello-python
```
#### Installation sur Linux 

```bash
python3 -m pip install tello tello-python
```