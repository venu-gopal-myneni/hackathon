from main import main
from pprint import pprint
from pathlib import Path

FILE_DIR = Path(__file__).parent.parent
folder_path = Path(FILE_DIR, "sample_data")
output = main(folder_path)
pprint(output)