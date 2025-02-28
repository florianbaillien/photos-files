import os
import shutil

# Extensions des fichiers multimédias
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"}
VIDEO_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm"}
ALL_EXTENSIONS = IMAGE_EXTENSIONS | VIDEO_EXTENSIONS

def collect_media_files(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    for root, _, files in os.walk(source_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = os.path.splitext(file)[-1].lower()
            
            if file_ext in ALL_EXTENSIONS:
                shutil.move(file_path, os.path.join(target_dir, file))
                print(f"Déplacé: {file_path} -> {target_dir}")

if __name__ == "__main__":
    source_directory = input("Entrez le répertoire source : ")
    target_directory = os.path.join(source_directory, "Media")
    collect_media_files(source_directory, target_directory)
    print("Opération terminée.")
