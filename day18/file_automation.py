from pathlib import Path
import shutil

def organize_folder(folder_path: str):
    folder = Path(folder_path)

    for item in folder.iterdir():
        if item.is_file():
            extension = item.suffix.replace(".", "")
            if not extension:
                extension = "no_extension"
        
            destination = folder / extension
            destination.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination / item.name))
            print(f"Moved {item.name} -> {extension}/")

organize_folder("messy_folder")