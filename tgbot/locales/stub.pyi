from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    dlg: Dlg
    btn: Btn


class Cmd:
    start: CmdStart
    psychology: CmdPsychology
    tests: CmdTests
    profile: CmdProfile


class CmdStart:
    @staticmethod
    def __call__() -> Literal["""/start"""]: ...

    @staticmethod
    def description() -> Literal["""Начать вё сначала"""]: ...


class CmdPsychology:
    @staticmethod
    def __call__() -> Literal["""/psychology"""]: ...

    @staticmethod
    def description() -> Literal["""Мой личный психолог"""]: ...


class CmdTests:
    @staticmethod
    def __call__() -> Literal["""/tests"""]: ...

    @staticmethod
    def description() -> Literal["""Тесты: психологические и не только"""]: ...


class CmdProfile:
    @staticmethod
    def __call__() -> Literal["""/profile"""]: ...

    @staticmethod
    def description() -> Literal["""О себе: кто вы и как ваше самочувствие?"""]: ...


class Dlg:
    win: DlgWin

    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
/psychology - пообщайтесь с психологом
/tests - пройдите тесты и узнайте больше о себе
/profile - добавьте информацию о себе и составьте свой психологический профиль"""]: ...

    @staticmethod
    def psychology() -> Literal["""&lt;b&gt;Мой личный психолог&lt;/b&gt;

Психолог пообщается с вами и постарается улучшить ваше психологическое самочувствие.

Будьте искренни и доброжелательны."""]: ...

    @staticmethod
    def tests() -> Literal["""&lt;b&gt;Тесты: психологические и не только&lt;/b&gt;

Пройдите психологический тест, чтобы лучше понять себя.

Чем больше вы знаете о себе, тем проще вам и вашим окружающим понимать вас и общаться с вами.
Знайте: все люди разные, и кем бы вы не хотели казаться самому себе, ваша природа останется той как она есть.
Тест не даёт критической оценки: хорошо или плохо. Тест раскрывает вашу природу.

Если вы чувствуете, что в вашей жизни что-то не так, то наверняка причина кроется в неправильном представлении о себе.
Тест поможет вам найти эти пробелы.

Если вы чувствуете, что в вашей жизни всё идёт хорошо, то скорее всего вы хорошо знаете себя. Это здорово!
Тест добавит вам частичку этого знания.

В добрый путь к самопознанию!"""]: ...

    @staticmethod
    def profile() -> Literal["""&lt;b&gt;О себе: кто вы и как ваше самочувствие?&lt;/b&gt;

Создайте свой профиль и добавьте данные о себе.

Вы можете пройти психологический тест, чтобы составить свой психологический портрет.
Бот будет использовать ваши данные в общении с вами и лучше понимать вас.

Ответьте на несколько простых вопросов.
Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время."""]: ...


class DlgWin:
    @staticmethod
    def profile() -> Literal["""= &lt;b&gt;&lt;/b."""]: ...


class Btn:
    start: BtnStart
    choose: BtnChoose
    about: BtnAbout

    @staticmethod
    def back() -> Literal["""Вернуться"""]: ...

    @staticmethod
    def save() -> Literal["""Сохранить"""]: ...


class BtnStart:
    @staticmethod
    def session() -> Literal["""Начать сеанс"""]: ...

    @staticmethod
    def test() -> Literal["""Выбрать тест"""]: ...


class BtnChoose:
    @staticmethod
    def test() -> Literal["""Выбрать тест"""]: ...


class BtnAbout:
    @staticmethod
    def me() -> Literal["""О себе"""]: ...

