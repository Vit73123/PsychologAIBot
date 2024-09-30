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
from tgbot.tools.json import load_json
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
        config: Config,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Appointment: get_appointment: context: %s", dialog_manager.current_context())
    log_dev.debug(" Appointment: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    state_data = await state.get_data()

    # Создаём промпт и инициализируем ChatGPT, если его нет в контексте FSM
    if 'gpt' not in state_data:
        user_id = dialog_manager.start_data['user_id']

        # Создаём экземпляр сервиса GPT текущего пользователя
        config.gpt.prompts_info = load_json(config.root_path / 'tgbot' / 'config' / 'prompts_info.json')
        gpt = ChatGptService(token=config.gpt.token, url=config.gpt.url)

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
        # Т.к. с ChatGPT взаимодействуют разные пользователи, то необходимо сохранять
        # целый экземпляр сервиса GPT, который содержит весь необходимый контекст:
        # - client - уникальный идентификатор клиента (пользователя), который направил запрос в ChatGPT
        # - model - на будущее, когда разные пользователи смогут подключать разные модели ChatGPT
        # - messages_list - все реплики диалога, начиная с промпта и обращения
        #
        # Для каждого сеанса каждого пользователя необходимо создавать свой
        # новый экземпляр сервиса GPT, т.к. client назначается экземпляру сервиса.
        #
        # Если использовать один общий для всех пользователей экземпляр GPT, то
        # у все пользователи будут выступать как один клиент,
        # и ChatGPT на сервере будет объединять их реплики в одном своём общем контексте
        await state.update_data({'gpt': gpt})

    # Обрабатываем ответ ChatGPT, если он в контексте FSM, т.е. уже идёт диалог
    else:

        # Получаем экземпляр сервиса GPT из FSM текущего пользователя
        gpt: ChatGptService = await get_state_data(key='gpt', state=state)

        # Получаем из виджета TextInput сообщение пользователя
        text: str = dialog_manager.current_context().widget_data.get('inp_message')

        # Отправляем в ChatGPT сообщение. Cервис GPT под капотом обновляет свой messages_list
        answer: str = await gpt.add_message(text)

        # Обновляем экземпляр сервиса GPT в FSM текущего пользователя
        await state.update_data({'gpt': gpt})

        log_dev.debug(" Appointment: chat: FSM: context: %s", await state.get_data())

    return {
        "btn_appointment_stop": i18n.btn.psychology.appointment.stop(),
        "gpt_message": answer
    }


# Ревью
async def get_review(
        dialog_manager: DialogManager,
        state: FSMContext,
        repo: Repo,
        i18n: TranslatorRunner,
        **kwargs
) -> dict[str, str]:
    log_dev.debug(" Review: review: context: %s", dialog_manager.current_context())
    log_dev.debug(" Review: get_start: FSM: state: %s, context: %s", await state.get_state(), await state.get_data())

    await state.set_state(Psychology.review)

    # Инициализируем сервис GPT текущего пользователя
    gpt: ChatGptService = await get_state_data(key='gpt', state=state)

    # Отправляем в ChatGPT сообщение с просьбой сделать ревью сеанса
    text: str = i18n.gpt.pmt.psycholog.finish.createreview()
    answer: str = await gpt.add_message(text)

    # Удаляем сервис GPT из контекста FSM текущего пользователя
    data = await state.get_data()
    del data['gpt']
    await state.set_data(data)

    # Очищаем данные виджетов:


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
