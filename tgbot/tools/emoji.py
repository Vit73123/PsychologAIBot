from pathlib import Path

from tgbot.tools.json import load_json


def load_emoji_grades(path: Path) -> dict:
    return load_json(path / 'emoji.json')
