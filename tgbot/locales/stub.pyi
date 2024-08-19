from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    dlg: Dlg


class Cmd:
    @staticmethod
    def start() -> Literal["""/start"""]: ...

    @staticmethod
    def psychology() -> Literal["""/psychology"""]: ...

    @staticmethod
    def tests() -> Literal["""/tests"""]: ...

    @staticmethod
    def profile() -> Literal["""/profile"""]: ...


class Dlg:
    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
/psychology - пообщайтесь с психологом
/tests - пройдите тесты и узнайте больше о себе
/profile - добавьте информацию о себе и составьте свой психологический профиль"""]: ...

