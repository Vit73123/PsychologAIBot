from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    win: Win
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


class Win:
    start: WinStart
    psychology: WinPsychology
    tests: WinTests
    profile: WinProfile


class WinStart:
    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
/psychology - пообщайтесь с психологом
/tests - пройдите тесты и узнайте больше о себе
/profile - добавьте информацию о себе и составьте свой психологический профиль"""]: ...


class WinPsychology:
    @staticmethod
    def start() -> Literal["""&lt;b&gt;Мой личный психолог&lt;/b&gt;

Психолог пообщается с вами и постарается улучшить ваше психологическое самочувствие.

Будьте искренни и доброжелательны."""]: ...


class WinTests:
    @staticmethod
    def start() -> Literal["""&lt;b&gt;Тесты: психологические и не только&lt;/b&gt;

Пройдите психологический тест, чтобы лучше понять себя.

Чем больше вы знаете о себе, тем проще вам и вашим окружающим понимать вас и общаться с вами.
Знайте: все люди разные, и кем бы вы не хотели казаться самому себе, ваша природа останется той как она есть.
Тест не даёт критической оценки: хорошо или плохо. Тест раскрывает вашу природу.

Если вы чувствуете, что в вашей жизни что-то не так, то наверняка причина кроется в неправильном представлении о себе.
Тест поможет вам найти эти пробелы.

Если вы чувствуете, что в вашей жизни всё идёт хорошо, то скорее всего вы хорошо знаете себя. Это здорово!
Тест добавит вам частичку этого знания.

В добрый путь к самопознанию!"""]: ...


class WinProfile:
    @staticmethod
    def start() -> Literal["""&lt;b&gt;О себе: кто вы и как ваше самочувствие?&lt;/b&gt;

Создайте свой профиль и добавьте данные о себе.

Вы можете пройти психологический тест, чтобы составить свой психологический портрет.
Бот будет использовать ваши данные в общении с вами и лучше понимать вас.

Ответьте на несколько простых вопросов.
Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время."""]: ...

    @staticmethod
    def aboutme() -> Literal["""= &lt;b&gt;&lt;/b."""]: ...


class Btn:
    psychology: BtnPsychology
    tests: BtnTests
    profile: BtnProfile

    @staticmethod
    def back() -> Literal["""Вернуться"""]: ...

    @staticmethod
    def save() -> Literal["""Сохранить"""]: ...

    @staticmethod
    def ok() -> Literal["""Ok"""]: ...

    @staticmethod
    def cancel() -> Literal["""Отменить"""]: ...


class BtnPsychology:
    start: BtnPsychologyStart


class BtnPsychologyStart:
    @staticmethod
    def session() -> Literal["""Начать сеанс"""]: ...


class BtnTests:
    start: BtnTestsStart


class BtnTestsStart:
    @staticmethod
    def choosetest() -> Literal["""Выбрать тест"""]: ...

    @staticmethod
    def dotest() -> Literal["""Пройти тест"""]: ...


class BtnProfile:
    start: BtnProfileStart
    aboutme: BtnProfileAboutme


class BtnProfileStart:
    @staticmethod
    def aboutme() -> Literal["""О себе"""]: ...


class BtnProfileAboutme:
    @staticmethod
    def name() -> Literal["""Меня зовут:"""]: ...

    @staticmethod
    def mail() -> Literal["""[М ]"""]: ...

    @staticmethod
    def femail() -> Literal["""[Ж ]"""]: ...

    @staticmethod
    def age() -> Literal["""Мне лет:"""]: ...

    @staticmethod
    def status() -> Literal["""Как я себя чуствую?"""]: ...

