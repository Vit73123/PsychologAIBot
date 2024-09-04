import json
from pathlib import Path


def load_json(path: Path) -> dict:
    with open(path, encoding='utf-8') as f:
        json_data = json.load(f)
    return json_data
