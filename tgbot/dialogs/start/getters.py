from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from tgbot.services.logger import get_logger_dev

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


async def get_start(
        i18n: TranslatorRunner,
        state: FSMContext,
        **kwargs
) -> dict[str, str]:
    log.info(" state: %s", await state.get_data())
    state_data = await state.get_data()

    return {
        'dlg_start': i18n.dlg.start(),
        'username': state_data.get('username')
    }
