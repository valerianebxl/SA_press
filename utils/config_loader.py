import json
import datetime
import os

def load_config(config_file):
    """Charge la configuration du projet depuis un fichier JSON."""
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"⚠️ Fichier de configuration introuvable : {config_file}")

    with open(config_file, "r", encoding="utf-8") as file:
        config = json.load(file)

    # Convertir les dates en objets datetime
    config["start_date"] = datetime.datetime.strptime(config["start_date"], "%Y-%m-%d")
    config["end_date"] = datetime.datetime.strptime(config["end_date"], "%Y-%m-%d")

    return config
