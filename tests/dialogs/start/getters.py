from logging import getLogger

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from tgbot.db import Repo
from tgbot.db.dao import UserDAO
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(dialog_manager: DialogManager,
                    state: FSMContext,
                    repo: Repo, **kwargs
                    ) -> dict[str, str]:
    log.debug(" Start: get_start")

    state_data = await state.get_data()
    log_dev.debug(" Start: state: %s", await state.get_data())

    log_dev.debug(" Start: dialog context: %s", dialog_manager.current_context())
    log_dev.debug(" Start: dialog state: items : %s", dialog_manager.dialog_data.items())
    log_dev.debug(" Start: dialog state: keys  : %s", dialog_manager.dialog_data.keys())
    log_dev.debug(" Start: dialog state: values: %s", dialog_manager.dialog_data.values())

    user_id: int = state_data['user_id']
    user: UserDAO = await repo.user.get(user_id)

    dialog_manager.dialog_data.update(user_id=user_id)
    dialog_manager.dialog_data.update(user=user)

    log_dev.debug(" Start: user id: %s", dialog_manager.dialog_data.get('user_id'))
    log_dev.debug(" Start: user: %s", user)
    log_dev.debug(" Start: dialog context: %s", dialog_manager.current_context())

    log_dev.debug(" Start: dialog state: items : %s", dialog_manager.dialog_data.items())
    log_dev.debug(" Start: dialog state: keys  : %s", dialog_manager.dialog_data.keys())
    log_dev.debug(" Start: dialog state: values: %s", dialog_manager.dialog_data.values())

    return {
        'user': dialog_manager.dialog_data.get('user')
    }
