from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    @staticmethod
    def start(*, cmd_psychology, cmd_tests, cmd_profile) -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
/{ $cmd_psychology } - пообщайтесь с психологом
/{ $cmd_tests } - пройдите тесты и узнайте больше о себе
/{ $cmd_profile } - добавьте информацию о себе и составьте свой психологический профиль"""]: ...

