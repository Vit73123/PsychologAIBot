from logging import getLogger

import openai
from openai import OpenAI

from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


class ChatGptService:
    client: OpenAI = None
    model: str = ''
    messages_list: list = None

    def __init__(self, token, url, model: str = 'gpt-3.5-turbo'):
        self.client = openai.OpenAI(
            base_url=url,
            api_key=token)
        self.model = model
        self.messages_list = []

    async def _send_message_list(self) -> str:
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages_list,
            max_tokens=3000,
            temperature=0.9
        )
        message = completion.choices[0].message
        self.messages_list.append(message)
        return message.content

    def set_prompt(self, prompt_text: str) -> None:
        log_dev.debug(" Set prompt: %s", prompt_text)
        self.messages_list.clear()
        self.messages_list.append({"role": "system", "content": prompt_text})
        log_dev.debug(" Set prompt: messages_list: %s", self.messages_list)

    async def add_prompt(self, prompt_text: str) -> str:
        log_dev.debug(" Add prompt: %s", prompt_text)
        self.messages_list.append({"role": "system", "content": prompt_text})
        log_dev.debug(" Set prompt: messages_list: %s", self.messages_list)
        return await self._send_message_list()

    async def add_message(self, message_text: str) -> str:
        self.messages_list.append({"role": "user", "content": message_text})
        log_dev.debug(" Set prompt: messages_list: %s", self.messages_list)
        return await self._send_message_list()

    async def send_question(self, prompt_text: str, message_text: str) -> str:
        self.messages_list.clear()
        self.messages_list.append({"role": "system", "content": prompt_text})
        self.messages_list.append({"role": "user", "content": message_text})
        # return await self._send_message_list()

    # def set_messages_list(self, messages_list: list) -> None:
    #     self.messages_list = messages_list
