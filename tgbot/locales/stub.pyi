from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    emoji: Emoji
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


class Emoji:
    i: EmojiI
    me: EmojiMe
    psychologist: EmojiPsychologist

    @staticmethod
    def home() -> Literal["""🏠"""]: ...

    @staticmethod
    def pin() -> Literal["""📌"""]: ...

    @staticmethod
    def check() -> Literal["""✅"""]: ...

    @staticmethod
    def soon() -> Literal["""✴"""]: ...

    @staticmethod
    def new() -> Literal["""🆕"""]: ...

    @staticmethod
    def next() -> Literal["""▶"""]: ...

    @staticmethod
    def back() -> Literal["""◀"""]: ...

    @staticmethod
    def skip() -> Literal["""⏭"""]: ...

    @staticmethod
    def clear() -> Literal["""🧹"""]: ...

    @staticmethod
    def up() -> Literal["""⤴️"""]: ...

    @staticmethod
    def setback() -> Literal["""↪"""]: ...

    @staticmethod
    def save() -> Literal["""💾"""]: ...

    @staticmethod
    def ok() -> Literal["""☑️"""]: ...

    @staticmethod
    def cancel() -> Literal["""✖"""]: ...

    @staticmethod
    def male() -> Literal["""♂"""]: ...

    @staticmethod
    def female() -> Literal["""♀"""]: ...

    @staticmethod
    def grade() -> Literal["""📶"""]: ...

    @staticmethod
    def tests() -> Literal["""📝"""]: ...


class EmojiI:
    @staticmethod
    def hi() -> Literal["""🙋"""]: ...

    @staticmethod
    def profile() -> Literal["""👤"""]: ...

    @staticmethod
    def am() -> Literal["""🙎"""]: ...

    @staticmethod
    def wrong() -> Literal["""💁"""]: ...

    @staticmethod
    def oh() -> Literal["""🤷"""]: ...


class EmojiMe:
    @staticmethod
    def important() -> Literal["""❤️‍🔥"""]: ...


class EmojiPsychologist:
    @staticmethod
    def man() -> Literal["""🕵️‍♂️"""]: ...

    @staticmethod
    def woman() -> Literal["""🕵️‍♀️"""]: ...


class Win:
    aboutme: WinAboutme

    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;

Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

Выбирайте:
📌 &lt;b&gt;Тесты&lt;/b&gt; - пройдите тесты и узнайте больше о себе &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;
📌 &lt;b&gt;О себе&lt;/b&gt; - добавьте информацию о себе,
составьте свой психологический профиль &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;"""]: ...

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

📌 Создайте свой профиль и добавьте данные о себе. 👤

📌 Вы можете пройти психологический тест, чтобы составить свой психологический портрет. 🕵️‍♀️
Бот будет использовать ваши данные в общении с вами и лучше понимать вас. &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;

📌 Ответьте на несколько простых вопросов. 📝
Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время."""]: ...


class WinAboutmeProfile:
    h: WinAboutmeProfileH
    name: WinAboutmeProfileName
    age: WinAboutmeProfileAge

    @staticmethod
    def gender() -> Literal["""&lt;b&gt;🙋 Я&lt;/b&gt;

✅ Мне бы хотелось, чтобы меня не путали с тем, кем я не являюсь."""]: ...

    @staticmethod
    def status() -> Literal["""&lt;b&gt;Хочу рассказать, что для меня сейчас важнее всего: ‼&lt;/b&gt;

✅ В настоящее время и в ближайщем будущем - лично для меня и моего самочувствия?
✅ Какую проблему решаем?
✅ Что направляет мои мысли, мои эмоции, мои действия?
✅ Есть ли проблема, которая беспокоит меня больше всего?
✅ Как я чувствую себя в целом, как настроение?"""]: ...

    @staticmethod
    def grade() -> Literal["""Как я оценил бы уровень своего эмоционального состояния?"""]: ...


class WinAboutmeProfileH:
    @staticmethod
    def status() -> Literal["""&lt;b&gt;❤️‍🔥 Для меня сейчас важно:&lt;/b&gt;"""]: ...

    @staticmethod
    def grade() -> Literal["""&lt;b&gt;📶 Моё состояние:&lt;/b&gt;"""]: ...


class WinAboutmeProfileName:
    @staticmethod
    def __call__() -> Literal["""✅ Теперь ко мне будут обращаться так, каким именем я представляюсь."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;💁 Я ошибся:&lt;/b&gt;

✅ В имени не должно быть ничего лишнего:
цифры, знаки и т.п., 🤷"""]: ...


class WinAboutmeProfileAge:
    @staticmethod
    def __call__() -> Literal["""&lt;b&gt;🙋 Мой возраст:&lt;/b&gt;

✅ В общении люди всегда учитывают возраст собеседника."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;💁 Я ошибся:&lt;/b&gt;

✅ Вряд ли мне меньше 5 или больше 150 лет,
или я укажу возраст чем-нибудь, кроме числа. 🤷"""]: ...


class Btn:
    getback: BtnGetback
    cancel: BtnCancel
    start: BtnStart
    psychology: BtnPsychology
    tests: BtnTests
    aboutme: BtnAboutme

    @staticmethod
    def next() -> Literal["""Вперёд ▶"""]: ...

    @staticmethod
    def back() -> Literal["""Назад ◀"""]: ...

    @staticmethod
    def home() -> Literal["""Главное меню 🏠"""]: ...

    @staticmethod
    def skip() -> Literal["""Попустить ⏭"""]: ...

    @staticmethod
    def clear() -> Literal["""Сброс 🧹"""]: ...

    @staticmethod
    def setback() -> Literal["""Вернуть ↪"""]: ...

    @staticmethod
    def save() -> Literal["""Сохранить 💾"""]: ...

    @staticmethod
    def ok() -> Literal["""Ok ☑️"""]: ...


class BtnGetback:
    @staticmethod
    def __call__() -> Literal["""Назад ⤴️"""]: ...

    @staticmethod
    def home() -> Literal["""Вернуться в главное меню 🏠"""]: ...


class BtnCancel:
    @staticmethod
    def __call__() -> Literal["""Отмена ✖"""]: ...

    @staticmethod
    def getback() -> Literal["""Отмена ⤴️"""]: ...


class BtnStart:
    @staticmethod
    def psychology() -> Literal["""Сеанс с психологом 🕵️‍♀️"""]: ...

    @staticmethod
    def tests() -> Literal["""Тесты 📝"""]: ...

    @staticmethod
    def aboutme() -> Literal["""О себе 👤"""]: ...


class BtnPsychology:
    appointment: BtnPsychologyAppointment


class BtnPsychologyAppointment:
    @staticmethod
    def start() -> Literal["""Начать сеанс"""]: ...

    @staticmethod
    def new() -> Literal["""Новый сеанс"""]: ...

    @staticmethod
    def follow() -> Literal["""Продолжить сеанс"""]: ...

    @staticmethod
    def stop() -> Literal["""Звершить сеанс"""]: ...

    @staticmethod
    def thankyou() -> Literal["""Спасибо!"""]: ...


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
    gender: BtnAboutmeProfileGender

    @staticmethod
    def __call__() -> Literal["""О себе 🙋"""]: ...

    @staticmethod
    def name() -> Literal["""Имя 🙎"""]: ...

    @staticmethod
    def age() -> Literal["""Возраст 🙎"""]: ...

    @staticmethod
    def status() -> Literal["""Сейчас важно! ❤️‍🔥"""]: ...

    @staticmethod
    def grade() -> Literal["""Оценка состояния 📶"""]: ...


class BtnAboutmeProfileGender:
    @staticmethod
    def __call__() -> Literal["""Пол 🙎"""]: ...

    @staticmethod
    def male() -> Literal["""М ♂"""]: ...

    @staticmethod
    def female() -> Literal["""Ж ♀"""]: ...


class Gpt:
    pmt: GptPmt


class GptPmt:
    psycholog: GptPmtPsycholog


class GptPmtPsycholog:
    person: GptPmtPsychologPerson
    finish: GptPmtPsychologFinish


class GptPmtPsychologPerson:
    name: GptPmtPsychologPersonName
    age: GptPmtPsychologPersonAge
    gender: GptPmtPsychologPersonGender

    @staticmethod
    def data() -> Literal["""Учитывайте следующие данные обо мне:"""]: ...

    @staticmethod
    def status() -> Literal["""В настоящее время особую важность для меня представляет следующее:"""]: ...

    @staticmethod
    def review() -> Literal["""Ваши выводы из нашего последнего сеанса общения с вами:"""]: ...


class GptPmtPsychologPersonName:
    @staticmethod
    def __call__() -> Literal["""меня зовут"""]: ...

    @staticmethod
    def anoninm() -> Literal["""я не хочу называть своего имени"""]: ...


class GptPmtPsychologPersonAge:
    @staticmethod
    def __call__() -> Literal["""мой возраст"""]: ...

    @staticmethod
    def anonim() -> Literal["""мой возраст останется неизвестен"""]: ...


class GptPmtPsychologPersonGender:
    @staticmethod
    def __call__() -> Literal["""пол человека"""]: ...

    @staticmethod
    def anonim() -> Literal["""мой пол останется неизвестен"""]: ...


class GptPmtPsychologFinish:
    @staticmethod
    def createreview() -> Literal["""Дайте развёрнутую характеристику моему психологическому состоянию по итогам всего нашего диалога, принимая во внимание все ваши знания из области психологии, психоанализа, конфликтологии, психиатрии, социальных наук, а также вашего общения с другими людьми. Выделите и сформулируйте конкретные проблемные вопросы так, чтобы вы могли продолжить наш разговор и обсудить со мной все эти вопросы в будущем. Не полагайтесь только на беседу в этот раз, а обязательно примите во внимание то, какой была ваша последняя оценка, с которой вы начали разговор со мной."""]: ...


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
    def before() -> Literal["""меня зовут"""]: ...


class TxtAge:
    @staticmethod
    def before() -> Literal["""мне"""]: ...

    @staticmethod
    def after() -> Literal["""лет"""]: ...


class TxtGender:
    @staticmethod
    def before() -> Literal["""я"""]: ...

    @staticmethod
    def male() -> Literal["""мужчина"""]: ...

    @staticmethod
    def femail() -> Literal["""женщина"""]: ...


class Srv:
    name: SrvName


class SrvName:
    @staticmethod
    def checkname() -> Literal["""^[а-яА-ЯёЁ ]+"""]: ...

