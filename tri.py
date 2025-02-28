import os
import shutil
from datetime import datetime

# Définir le dossier source contenant les images
source_folder = "{path}"

# Vérifier si le dossier existe
if not os.path.exists(source_folder):
    print("Le dossier source n'existe pas.")
    exit()

# Extensions d'images à traiter
image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}

# Parcourir les fichiers du dossier
for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    # Vérifier si c'est un fichier image
    if os.path.isfile(file_path) and any(filename.lower().endswith(ext) for ext in image_extensions):
        # Obtenir la date de modification du fichier
        mod_time = os.path.getmtime(file_path)
        mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

        # Créer le dossier cible avec la date
        target_folder = os.path.join(source_folder, mod_date)
        os.makedirs(target_folder, exist_ok=True)

        # Déplacer le fichier dans le dossier correspondant
        shutil.move(file_path, os.path.join(target_folder, filename))
        print(f"Déplacé : {filename} → {target_folder}/")
