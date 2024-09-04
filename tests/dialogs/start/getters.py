from logging import getLogger
from typing import TYPE_CHECKING

from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager
from fluentogram import TranslatorRunner

from tgbot.db import Repo
from tgbot.tools.logger import get_logger_dev

log = getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)

if TYPE_CHECKING:
    from tgbot.locales.stub import TranslatorRunner


async def get_start(dialog_manager: DialogManager,
                    state: FSMContext,
                    repo: Repo,
                    i18n: TranslatorRunner,
                    **kwargs
                    ) -> dict[str, str]:
    log_dev.debug(" Start: get_start: context: %s", dialog_manager.current_context())

    return {
        "emoji-home": i18n.emoji.home(),
        "emoji-pin": i18n.emoji.pin(),
        "emoji-soon": i18n.emoji.soon(),
        "emoji-new": i18n.emoji.new(),
        "emoji-next": i18n.emoji.next(),
        "emoji-back": i18n.emoji.back(),
        "emoji-skip": i18n.emoji.skip(),
        "emoji-clear": i18n.emoji.clear(),
        "emoji-getback": i18n.emoji.getback(),
        "emoji-setback": i18n.emoji.setback(),
        "emoji-save": i18n.emoji.save(),
        "emoji-ok": i18n.emoji.ok(),
        "emoji-cancel": i18n.emoji.cancel(),

        "emoji-i-hi": i18n.emoji.i.hi(),
        "emoji-i-profile": i18n.emoji.i.profile(),
        "emoji-i-am": i18n.emoji.i.am(),

        "emoji-i-wrong": i18n.emoji.i.wrong(),
        "emoji-i-oh": i18n.emoji.i.oh(),
        "emoji-male": i18n.emoji.male(),
        "emoji-female": i18n.emoji.female(),

        "emoji-me-important": i18n.emoji.me.important(),
        "emoji-grade": i18n.emoji.grade(),
        "emoji-psychologist-man": i18n.emoji.psychologist.man(),
        "emoji-psychologist-woman": i18n.emoji.psychologist.woman(),

        "win-start": i18n.win.start(),
        "win-aboutme": i18n.win.aboutme(),

        "btn-home": i18n.btn.home(),
        "btn-getback-home": i18n.btn.getback.home(),

    }
