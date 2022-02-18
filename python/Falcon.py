# Importation du module de configuration
from config.config import Config
globalConfig = Config("config.json")        # Fichier de configuration du drone
logConfig = Config("logs/log_meta.json")    # Fichier de configuration des logs

# Importation du module d'affichage graphique (Interface utilisateur)
# **Vide**

