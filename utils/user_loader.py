import json
from pathlib import Path


def load_users():
    project_root = Path(__file__).resolve().parent.parent
    file_path = project_root / "resources" / "usersData.json"

    with open(file_path, "r") as f:
        return json.load(f)
