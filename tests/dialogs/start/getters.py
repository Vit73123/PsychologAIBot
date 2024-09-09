from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.config import Config
from tgbot.db import Repo
from tgbot.db.dao import UserDAO, StatusDAO
from tgbot.services.gpt import ChatGptService
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import get_state_data

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


# GPT

# Start
async def get_start(
        state: FSMContext,
        config: Config,
        repo: Repo,
        dialog_manager: DialogManager,
        gpt: ChatGptService,
        i18n: TranslatorRunner,

        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Test: get_grade: context: %s", dialog_manager.current_context())
    log_dev.debug(" Test: get_grade: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    radio_test = [
        ('A', '1'),
        ('B', '2'),
    ]

    # user: UserDAO = await repo.user.get(1)
    # status: StatusDAO = await repo.status.get_last_by_user_id(1)
    # appointment: AppointmentDAO = await repo.appointment.get_last_by_user_id(1)

    # prompt = create_prompt(person_data=)

    # prompt_intro = {
    #     'role': 'system',
    #     'text': get_prompt(prompt_itro, config)
    # }
    # gpt = {
    #     'messages_list': [prompt_intro]
    # }
    # await state.update_data(gpt)
    #
    # log_dev.debug(" Start: get_start: context: %s", await state.get_data())
    #
    return {
        'radio_test': radio_test,
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
