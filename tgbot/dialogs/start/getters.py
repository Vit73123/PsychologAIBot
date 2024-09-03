from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.db.dao import UserDAO
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(dialog_manager: DialogManager,
                    i18n: TranslatorRunner,
                    state: FSMContext,
                    repo: Repo,
                    **kwargs
                    ) -> dict[str, str]:
    log.debug(" Start: get_start")

    state_data = await state.get_data()

    user_id: int = state_data['user_id']
    user: UserDAO = await repo.user.get(user_id)

    dialog_manager.dialog_data.update(user_id=user_id)
    dialog_manager.dialog_data.update(user=user)

    return {
        'win_start': i18n.win.start(),
        'user': dialog_manager.dialog_data.get('user')
    }
