from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.tools.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

# Старт
async def get_start(dialog_manager: DialogManager,
                    state: FSMContext,
                    repo: Repo,
                    i18n: TranslatorRunner,
                    **kwargs
                    ) -> dict[str, str]:
    log.debug(" Start: get_start: context: %s", dialog_manager.current_context())

    user = dialog_manager.start_data.get('user')
    user['name'] = i18n.txt.name.anonim() if not user['name'] else user['name']

    return {
        'user': user,
        'win_start': i18n.win.start(),
        'btn_psychology': i18n.btn.start.psychology(),
        'btn_tests': i18n.btn.start.tests(),
        'btn_aboutme': i18n.btn.start.aboutme(),
    }
