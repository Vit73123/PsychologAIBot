import logging

from aiogram_dialog import DialogManager

from tgbot.tools.logger import get_logger_dev

log = logging.getLogger(__name__)
log_dev = get_logger_dev(__name__, log.level)


def item_get_value(item_id: str, dialog_manager: DialogManager) -> str:
    # log_dev.debug(" item_get_value: context: %s", dialog_manager.current_context())

    # item: ManagedTextInput | ManagedRadio = dialog_manager.find(item_id)

    widget_data = dialog_manager.current_context().widget_data
    if item_id in widget_data:
        log_dev.debug(" item_get_value: widget_data[]: %s", widget_data[item_id])
        return widget_data[item_id]

    # if isinstance(item, ManagedTextInput):
    #     log_dev.debug(" item_get_value: item class: %s", item.__class__.__name__)
    #     return item.get_value()
    # elif isinstance(item, ManagedRadio):
    #     log_dev.debug(" item_get_value: item class: %s", item.__class__.__name__)
    #     return item.get_checked()


def item_set_value(item_id: str, dialog_manager: DialogManager) -> str:
    # log_dev.debug(" item_get_value: context: %s", dialog_manager.current_context())

    # item: ManagedTextInput | ManagedRadio = dialog_manager.find(item_id)

    widget_data = dialog_manager.current_context().widget_data
    widget_data.update({f'{item_id}': '2'})
    if item_id in widget_data:
        log_dev.debug(" item_get_value: widget_data[]: %s", widget_data[item_id])
        return widget_data[item_id]
