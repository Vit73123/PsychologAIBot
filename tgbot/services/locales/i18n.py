from fluent_compiler.bundle import FluentBundle
from fluentogram import FluentTranslator, TranslatorHub


def create_translator_hub() -> TranslatorHub:
    translator_hub = TranslatorHub(
        locales_map={
            "ru": ("ru", "en"),
            "en": ("en", "ru")
        },
        translators=[
            FluentTranslator(
                locale="ru",
                translator=FluentBundle.from_files(
                    locale="ru-RU",
                    filenames=["tgbot/locales/ru/LC_MESSAGES/psychologaibot.ftl"])),
            FluentTranslator(
                locale="en",
                translator=FluentBundle.from_files(
                    locale="en-US",
                    filenames=["tgbot/locales/en/LC_MESSAGES/psychologaibot.ftl"]))
        ],
        root_locale="ru"
    )
    return translator_hub
