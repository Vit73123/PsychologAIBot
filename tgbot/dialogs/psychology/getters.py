from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

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
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Psychology: get_psychology: context: %s", dialog_manager.current_context())
    log_dev.debug(" Psychology: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    return {
        "win_psychology": i18n.win.psychology(),
        "btn_appointment_start": i18n.btn.psychology.appointment.start(),
        "btn_getback_home": i18n.btn.getback.home(),
    }


# Сеанс
async def get_appointment(
        dialog_manager: DialogManager,
        state: FSMContext,
        repo: Repo,
        gpt: ChatGptService,
        config: Config,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Appointment: get_appointment: context: %s", dialog_manager.current_context())
    log_dev.debug(" Appointment: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    state_data = await state.get_data()

    # Создаём промпт и инициализируем ChatGPT, если его нет в контексте FSM
    if 'gpt_context' not in state_data:
        user_id = dialog_manager.start_data['user_id']

        # Загружаем все данные, которые учитываются в промпте (user JOIN status JOIN appointment)
        appointment_data: dict = await repo.user.get_with_last_status_appointment(user_id)

        # Создаём промпт на загруженных данных
        prompt = create_prompt(user_data=appointment_data, config=config, i18n=i18n)

        # Инициализируем GPT:
        # - устанавливаемый начальный промпт - обращение к ChatGPT
        # - messages_list: в сервисе GPT под капотом создаётся список всех реплик диалога с ChatGPT
        gpt.set_prompt(prompt)

        # Отправляем в ChatGPT сообщение с просьбой начать диалог
        # в сервисе GPT под капотом обновляется его messages_list
        answer: str = await gpt.add_prompt("Пожалуйста, начни диалог.")

        # Сохраняем в FSM контекст GPT
        # Т.к. с ChatGPT взаимодействуют разные пользователи, то необходимо сохранять весь контекст
        # сервиса GPT:
        # - client - уникальный идентификатор клиента (пользователя), который направил запрос в ChatGPT
        # - model - на будущее, когда разные пользователи смогут подключать разные модели ChatGPT
        # - messages_list - все реплики диалога, начиная с промпта и обращения
        await state.update_data({'gpt_context': {
            'client': gpt.client,
            'model': gpt.model,
            'messages_list': gpt.messages_list,
        }})

    # Обрабатываем ответ ChatGPT, если он в контексте FSM, т.е. уже идёт диалог
    else:

        # Получаем текущий контекст GPT из FSM
        gpt_context = await get_state_data(key='gpt_context', state=state)

        # Инициализируем сервис GPT его текущим контекстом
        gpt.messages_list = gpt_context['messages_list']
        gpt.client = gpt_context['client']
        gpt.model = gpt_context['model']

        # Получаем из виджета TextInput сообщение пользователя
        text: str = dialog_manager.current_context().widget_data.get('inp_message')

        # Отправляем в ChatGPT сообщение. Cервис GPT под капотом обновляет свой messages_list
        answer: str = await gpt.add_message(text)

        # Обновляем текущий контекст GPT
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
    log_dev.debug(" Review: review: context: %s", dialog_manager.current_context())
    log_dev.debug(" Review: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    await state.set_state(Psychology.review)

    # Инициализируем сервис GPT его текущим контекстом
    gpt_context = await get_state_data(key='gpt_context', state=state)
    gpt.messages_list = gpt_context['messages_list']
    gpt.client = gpt_context['client']
    gpt.model = gpt_context['model']

    # Отправляем в ChatGPT сообщение с просьбой сделать ревью сеанса
    text: str = i18n.gpt.pmt.psycholog.finish.createreview()
    answer: str = await gpt.add_message(text)

    # Сохраняем ревью в базе данных
    await repo.appointment.add(
        AppointmentDAO(
            user_id=dialog_manager.start_data['user_id'],
            review=answer,
        )
    )
    log_dev.debug(" Appointment: chat: FSM: context: %s", await state.get_data())

    return {
        "btn_appointment_thankyou": i18n.btn.psychology.appointment.thankyou(),
        "gpt_message": answer
    }
