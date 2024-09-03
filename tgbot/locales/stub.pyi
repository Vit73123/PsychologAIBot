from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    win: Win
    btn: Btn
    gpt: Gpt
    txt: Txt
    srv: Srv


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
    aboutme: WinAboutme

    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
📌 &lt;b&gt;Сеанс с психологом&lt;/b&gt; - пообщайтесь с психологом
📌 &lt;b&gt;Тесты&lt;/b&gt; - пройдите тесты и узнайте больше о себе &lt;b&gt;[скоро!] ✴&lt;/b&gt;
📌 &lt;b&gt;О себе&lt;/b&gt; - добавьте информацию о себе,
составьте свой психологический профиль &lt;b&gt;[скоро!] ✴&lt;/b&gt;"""]: ...

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


class WinAboutme:
    profile: WinAboutmeProfile

    @staticmethod
    def __call__() -> Literal["""&lt;b&gt;О себе: кто вы и как ваше самочувствие?&lt;/b&gt;

📌 Создайте свой профиль и добавьте данные о себе.

📌 Вы можете пройти психологический тест, чтобы составить свой психологический портрет.
Бот будет использовать ваши данные в общении с вами и лучше понимать вас. &lt;b&gt;[скоро!] ✴&lt;/b&gt;

📌 Ответьте на несколько простых вопросов.
Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время."""]: ...


class WinAboutmeProfile:
    h: WinAboutmeProfileH
    name: WinAboutmeProfileName
    age: WinAboutmeProfileAge

    @staticmethod
    def state() -> Literal["""&lt;b&gt;Хочу рассказать, что для меня сейчас важнее всего: ‼&lt;/b&gt;

✅ В настоящее время и в ближайщем будущем - лично для меня и моего самочувствия?
✅ Какую проблему решаем?
✅ Что направляет мои мысли, мои эмоции, мои действия?
✅ Есть ли проблема, которая беспокоит меня больше всего?
✅ Как я чувствую себя в целом, как настроение?"""]: ...

    @staticmethod
    def grade() -> Literal["""Как я оценил бы уровень своего эмоционального состояния?"""]: ...


class WinAboutmeProfileH:
    @staticmethod
    def state() -> Literal["""&lt;b&gt;‼ Для меня сейчас важно: ‼&lt;/b&gt;"""]: ...

    @staticmethod
    def grade() -> Literal["""&lt;b&gt;Моё состояние: 🥵😧😟🙁🫤😏😑😌🙂😀😆&lt;/b&gt;"""]: ...


class WinAboutmeProfileName:
    @staticmethod
    def __call__() -> Literal["""&lt;b&gt;Моё имя: 🙋&lt;/b&gt;

✅ Ко мне будут обращаться так, как я представлюсь."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;Я ошибся: 💁&lt;/b&gt;

✅ В имени не должно быть ничего лишнего:
цифры, знаки и т.п., 🤷"""]: ...


class WinAboutmeProfileAge:
    @staticmethod
    def __call__() -> Literal["""&lt;b&gt;Солько мне лет: 🙋&lt;/b&gt;

✅ Возраст всегда присутствует в общении."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;Я ошибся: 💁&lt;/b&gt;

✅ Вряд ли мне меньше 5 или больше 150 лет,
или я укажу возраст чем-нибудь, кроме числа. 🤷"""]: ...


class Btn:
    back: BtnBack
    start: BtnStart
    psychology: BtnPsychology
    tests: BtnTests
    aboutme: BtnAboutme

    @staticmethod
    def next() -> Literal["""Вперёд"""]: ...

    @staticmethod
    def skip() -> Literal["""Попустить"""]: ...

    @staticmethod
    def save() -> Literal["""Сохранить"""]: ...

    @staticmethod
    def ok() -> Literal["""Ok"""]: ...

    @staticmethod
    def cancel() -> Literal["""Отмена"""]: ...


class BtnBack:
    @staticmethod
    def __call__() -> Literal["""Вернуться"""]: ...

    @staticmethod
    def start() -> Literal["""Главное меню"""]: ...


class BtnStart:
    @staticmethod
    def psychology() -> Literal["""Сеанс с психологом"""]: ...

    @staticmethod
    def tests() -> Literal["""Тесты"""]: ...

    @staticmethod
    def aboutme() -> Literal["""О себе"""]: ...


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


class BtnAboutme:
    profile: BtnAboutmeProfile


class BtnAboutmeProfile:
    @staticmethod
    def __call__() -> Literal["""О себе"""]: ...

    @staticmethod
    def name() -> Literal["""Меня зовут:"""]: ...

    @staticmethod
    def mail() -> Literal["""М"""]: ...

    @staticmethod
    def femail() -> Literal["""Ж"""]: ...

    @staticmethod
    def age() -> Literal["""Мне лет:"""]: ...

    @staticmethod
    def state() -> Literal["""Моё состояние"""]: ...


class Gpt:
    name: GptName


class GptName:
    @staticmethod
    def anonim() -> Literal["""Человек не хочет называть своего имени"""]: ...


class Txt:
    name: TxtName
    age: TxtAge
    gender: TxtGender

    @staticmethod
    def yearsstring1() -> Literal["""год"""]: ...

    @staticmethod
    def yearsstring2() -> Literal["""года"""]: ...

    @staticmethod
    def yearsstring3() -> Literal["""лет"""]: ...


class TxtName:
    @staticmethod
    def anonim() -> Literal["""Новый пользователь"""]: ...

    @staticmethod
    def before() -> Literal["""&lt;b&gt;Меня зовут&lt;/b&gt;"""]: ...


class TxtAge:
    @staticmethod
    def before() -> Literal["""&lt;b&gt;Мне&lt;/b&gt;"""]: ...

    @staticmethod
    def after() -> Literal["""&lt;b&gt;лет&lt;/b&gt;"""]: ...


class TxtGender:
    @staticmethod
    def before() -> Literal["""&lt;b&gt;Я&lt;/b&gt;"""]: ...

    @staticmethod
    def male() -> Literal["""мужчина"""]: ...

    @staticmethod
    def femail() -> Literal["""женщина"""]: ...


class Srv:
    name: SrvName


class SrvName:
    @staticmethod
    def checkname() -> Literal["""^[а-яА-ЯёЁ ]+"""]: ...

