# Importation des modules de configuration
import .core.config as config

config.Config("config", "config/config.json") # Fichier de configuration du drone
config.Config("logs", "logs/log_meta.json")   # Fichier de configuration des logs


# Importation des modules de journal
import core.logs as logs


