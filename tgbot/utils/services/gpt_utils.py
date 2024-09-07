from tgbot.config import Config
from tgbot.tools.json import load_json


def get_prompt(prompt_info: dict, config: Config) -> str:
    path = config.root_path / 'resources' / 'prompts' / 'prompts.json'
    prompt: str = load_prompt(prompt_info, path)

    return prompt


def get_prompt_info(category: str, config: Config) -> dict:
    return config.gpt.prompts_info[category]


def load_prompt(info: dict, path) -> str:
    prompts = load_json(path)
    return prompts[info['section']][info['subsection']][info['description']]
