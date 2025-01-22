
## **📌 Assembler les scripts en une mini-application **
# transformer ton script en une **interface utilisateur simple** avec `argparse` ou `Streamlit`.  

### ➡ **Avec `argparse` (ligne de commande)**
# spécifier les dates et les sources directement dans le terminal : 
import argparse
from utils.config_loader import load_config
from utils.file_utils import save_results_to_file

# Définir les arguments en ligne de commande
parser = argparse.ArgumentParser(description="Analyse des émotions dans la presse.")
parser.add_argument("--start", type=str, help="Date de début (YYYY-MM-DD)")
parser.add_argument("--end", type=str, help="Date de fin (YYYY-MM-DD)")

args = parser.parse_args()

# Charger la config et remplacer les dates si fournies
config = load_config("config/config.json")
if args.start:
    config["start_date"] = datetime.datetime.strptime(args.start, "%Y-%m-%d")
if args.end:
    config["end_date"] = datetime.datetime.strptime(args.end, "%Y-%m-%d")

# Exécuter l'analyse
save_results_to_file(config["relevant_sources"], config["start_date"], config["end_date"], config["output_dir"])
print("✅ Analyse terminée !")
