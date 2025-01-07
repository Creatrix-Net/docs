import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
try:
    import dotenv
    dotenv.load_dotenv(BASE_DIR/ os.path.join('config', '.env'))
    os.environ['path'] += r';C:\Program Files\UniConvertor-2.0rc5\dlls'
except:
    pass

os.system('mkdocs serve')