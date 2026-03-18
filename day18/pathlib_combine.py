from pathlib import Path
from datetime import date
import shutil, logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("backup")

def find_py_files(folder_path: str):
    folder = Path(folder_path)
    for item in folder.iterdir():
        if item.is_file() and item.suffix == ".py":
            logger.info(f"py file found: {item.name}")
            backup_folder = Path(folder / f"backup {date.today()}")
            backup_folder.mkdir(exist_ok=True)
            shutil.copy(str(item), str(backup_folder / item.name))
            logger.debug(f"{item.name} copied to {backup_folder.absolute()}")

find_py_files("py_files")