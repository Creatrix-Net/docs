import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

try:
    import dotenv
    dotenv.load_dotenv(BASE_DIR/ os.path.join('config', '.env'))
except:
    pass

os.system('mkdocs serve')