from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from tgbot.config import Config
from tgbot.services.gpt import ChatGptService
from tgbot.tools.logger import get_logger_dev
from tgbot.utils import get_prompt, get_state_data

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# GPT

# Start
async def get_start(
        state: FSMContext,
        config: Config,
        gpt: ChatGptService,
        i18n: TranslatorRunner,

        **kwargs
) -> dict[str, str]:
    log.debug(" GPT: get_start: context: %s", await state.get_data())

    prompt_info = config.gpt.prompts_info['psychology']
    prompt_intro = get_prompt(prompt_info, config)
    person_data = {
        
    }


    prompt_intro = {
        'role': 'system',
        'text': get_prompt(prompt_itro, config)
    }
    gpt = {
        'messages_list': [prompt_intro]
    }
    await state.update_data(gpt)

    log.debug(" Start: get_start: context: %s", await state.get_data())

    return {
    }


# Psychology
async def get_psychology(
        state: FSMContext,
        gpt: ChatGptService,

        **kwargs
) -> dict[str, str]:
    log.debug(" GPT: get_psychology: context: %s", await state.get_data())

    gpt_data: dict = await get_state_data('gpt', state)
    messages_list: list = gpt_data['messages_list']
    gpt.set_messages_list(messages_list)

    gpt_text = ''

    return {
        'gpt_text': gpt_text,
    }

