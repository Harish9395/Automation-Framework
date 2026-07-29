import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def load_environment(env="prod"):
    file_path = os.path.join(BASE_DIR, "config", "environments.yaml")

    with open(file_path) as f:
        data = yaml.safe_load(f)

    return data[env]["url"]
