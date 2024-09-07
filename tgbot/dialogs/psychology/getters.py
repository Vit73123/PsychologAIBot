from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tests.dialogs.states import Start
from tgbot.config import Config
from tgbot.db import Repo
from tgbot.db.dao import AppointmentDAO
from tgbot.dialogs.states import Psychology
from tgbot.services.gpt import ChatGptService
from tgbot.tools.logger import get_logger_dev
from tgbot.utils.dialogs import get_state_data, create_prompt

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


# Психология
async def get_psychology(
        dialog_manager: DialogManager,
        state: FSMContext,
        repo: Repo,
        gpt: ChatGptService,
        config: Config,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Psychology: get: context: %s", dialog_manager.current_context())
    log_dev.debug(" Psychology: get: state data: %s", await state.get_data())

    if await state.get_state() == Start.start:
        await state.set_state(Psychology.start)

        user_id = dialog_manager.start_data['user_id']
        user_data: dict = await repo.user.get_with_last_status_appointment(user_id)

        prompt = create_prompt(user_data=user_data, config=config, i18n=i18n)
        gpt.set_prompt(prompt)
        await state.update_data({'gpt_context': {
            'messages_list': gpt.messages_list
        }})

    log_dev.debug(" Psychology: get: state data: %s", await state.get_data())

    return {
        "win_psychology": i18n.win.psychology(),
        "btn_appointment_start": i18n.btn.psychology.appointment.start(),
        "btn_getback_home": i18n.btn.getback.home(),
    }


# Сеанс
async def get_appointment(
        dialog_manager: DialogManager,
        state: FSMContext,
        gpt: ChatGptService,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Appointment: get: context: %s", dialog_manager.current_context())
    log_dev.debug(" Appointment: get: FSM: context: %s", await state.get_data())

    if await state.get_state() == Psychology.start:
        gpt_context = await get_state_data(key='gpt_context', state=state)
        gpt.messages_list = gpt_context['messages_list']
        answer: str = await gpt.add_prompt("Пожалуйста, начни диалог.")
        await state.update_data({'gpt_context': {
            'client': gpt.client,
            'model': gpt.model,
            'messages_list': gpt.messages_list,
        }})
        await state.set_state(Psychology.appointment)
        log_dev.debug(" Appointment: start: get: FSM: context: %s", await state.get_data())
    else:
        gpt_context = await get_state_data(key='gpt_context', state=state)
        gpt.messages_list = gpt_context['messages_list']
        gpt.client = gpt_context['client']
        gpt.model = gpt_context['model']
        text: str = dialog_manager.current_context().widget_data.get('inp_message')
        answer: str = await gpt.add_message(text)
        gpt_context['messages_list'] = gpt.messages_list
        await state.update_data({'gpt_context': gpt_context})
        log_dev.debug(" Appointment: chat: FSM: context: %s", await state.get_data())

    return {
        "btn_appointment_stop": i18n.btn.psychology.appointment.stop(),
        "gpt_message": answer
    }


# Ревью
async def get_review(
        dialog_manager: DialogManager,
        state: FSMContext,
        gpt: ChatGptService,
        repo: Repo,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Appointment: review: context: %s", dialog_manager.current_context())
    log_dev.debug(" Appointment: review: FSM: context: %s", await state.get_data())

    await state.set_state(Psychology.review)
    gpt_context = await get_state_data(key='gpt_context', state=state)
    gpt.messages_list = gpt_context['messages_list']
    gpt.client = gpt_context['client']
    gpt.model = gpt_context['model']
    text: str = i18n.gpt.pmt.psycholog.finish.createreview()
    answer: str = await gpt.add_message(text)
    await repo.appointment.add(
        AppointmentDAO(
            user_id=dialog_manager.start_data['user_id'],
            review=answer,
        )
    )
    await state.set_state(Psychology.start)
    log_dev.debug(" Appointment: chat: FSM: context: %s", await state.get_data())

    return {
        "btn_appointment_thankyou": i18n.btn.psychology.appointment.thankyou(),
        "gpt_message": answer
    }
