from pathlib import Path
from string import Template

from dotenv import load_dotenv


def read_env_config():
    config_path = "/config/.env"
    root_path = Path(__file__).parent.parent.parent.parent

    dot_env_file_path = Template('$root$config').substitute(root=root_path, config=config_path)
    load_dotenv(dotenv_path=dot_env_file_path)
