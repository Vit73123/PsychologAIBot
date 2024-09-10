from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    cmd: Cmd
    emoji: Emoji
    txt: Txt
    srv: Srv
    win: Win
    gpt: Gpt
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


class Emoji:
    i: EmojiI
    hands: EmojiHands
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
    def reset() -> Literal["""↪"""]: ...

    @staticmethod
    def save() -> Literal["""💾"""]: ...

    @staticmethod
    def ok() -> Literal["""☑️"""]: ...

    @staticmethod
    def yes() -> Literal["""✔"""]: ...

    @staticmethod
    def no() -> Literal["""✖"""]: ...

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


class EmojiHands:
    @staticmethod
    def handshake() -> Literal["""🤝"""]: ...


class EmojiMe:
    @staticmethod
    def important() -> Literal["""❤️‍🔥"""]: ...


class EmojiPsychologist:
    @staticmethod
    def man() -> Literal["""🕵️‍♂️"""]: ...

    @staticmethod
    def woman() -> Literal["""🕵️‍♀️"""]: ...


class Txt:
    name: TxtName
    aboutme: TxtAboutme
    age: TxtAge
    gender: TxtGender

    @staticmethod
    def yearsstring1() -> Literal["""год"""]: ...

    @staticmethod
    def yearsstring2() -> Literal["""года"""]: ...

    @staticmethod
    def yearsstring3() -> Literal["""лет"""]: ...


class TxtName:
    before: TxtNameBefore

    @staticmethod
    def anonim() -> Literal["""Новый пользователь"""]: ...


class TxtAboutme:
    @staticmethod
    def menothing() -> Literal["""Я ещё ничего не рассказал о себе"""]: ...


class TxtNameBefore:
    long: TxtNameBeforeLong

    @staticmethod
    def short() -> Literal["""Меня зовут"""]: ...


class TxtNameBeforeLong:
    @staticmethod
    def v1() -> Literal["""Моё имя"""]: ...

    @staticmethod
    def v2() -> Literal["""Моё имя"""]: ...


class TxtAge:
    before: TxtAgeBefore

    @staticmethod
    def after() -> Literal["""лет"""]: ...


class TxtAgeBefore:
    long: TxtAgeBeforeLong

    @staticmethod
    def short() -> Literal["""Мне"""]: ...


class TxtAgeBeforeLong:
    @staticmethod
    def v1() -> Literal["""Мой возраст"""]: ...

    @staticmethod
    def v2() -> Literal["""Сколько мне лет"""]: ...


class TxtGender:
    before: TxtGenderBefore
    male: TxtGenderMale
    female: TxtGenderFemale


class TxtGenderBefore:
    long: TxtGenderBeforeLong

    @staticmethod
    def short() -> Literal["""Я"""]: ...


class TxtGenderBeforeLong:
    @staticmethod
    def v1() -> Literal["""Мой пол"""]: ...

    @staticmethod
    def v2() -> Literal["""Кто я - мужчина или женщина"""]: ...


class TxtGenderMale:
    @staticmethod
    def short() -> Literal["""М"""]: ...

    @staticmethod
    def long() -> Literal["""мужчина"""]: ...


class TxtGenderFemale:
    @staticmethod
    def short() -> Literal["""Ж"""]: ...

    @staticmethod
    def long() -> Literal["""женщина"""]: ...


class Srv:
    name: SrvName


class SrvName:
    @staticmethod
    def checkname() -> Literal["""^[а-яА-ЯёЁ ]+"""]: ...


class Win:
    profile: WinProfile
    name: WinName
    age: WinAge
    status: WinStatus
    yesno: WinYesno

    @staticmethod
    def start() -> Literal["""&lt;b&gt;Добро пожаловать в Бот психологической поддержки!&lt;/b&gt;
Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

&lt;b&gt;Выбирайте:&lt;/b&gt;
📌 &lt;b&gt;Сеанс с психологом&lt;/b&gt; - поговорите с психологом, поделитесь своей проблемой или радостью&lt;b&gt;
       Выберите своего психолога [скоро!] ✴🆕&lt;/b&gt;
📌 &lt;b&gt;Тесты&lt;/b&gt; - пройдите тесты и узнайте больше о себе &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;
📌 &lt;b&gt;О себе&lt;/b&gt; - добавьте информацию о себе.
       &lt;b&gt;Cоставьте свой психологический профиль&lt;/b&gt; &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;"""]: ...

    @staticmethod
    def psychology() -> Literal["""&lt;b&gt;Мой личный психолог&lt;/b&gt;

📌 Психолог пообщается с вами и постарается улучшить ваше психологическое самочувствие.

Будьте искренни и доброжелательны."""]: ...

    @staticmethod
    def tests() -> Literal["""&lt;b&gt;Тесты: психологические и не только&lt;/b&gt; &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;

📌 Пройдите психологический тест, чтобы лучше понять себя.

Чем больше вы знаете о себе, тем проще вам и вашим окружающим понимать вас и общаться с вами.
Знайте: все люди разные, и кем бы вы не хотели казаться самому себе, ваша природа останется той как она есть.
Тест не даёт критической оценки: хорошо или плохо. Тест раскрывает вашу природу.

В добрый путь к самопознанию!"""]: ...

    @staticmethod
    def aboutme() -> Literal["""&lt;b&gt;О себе: кто вы и как ваше самочувствие?&lt;/b&gt;

📌 Создайте свой профиль и добавьте данные о себе. 👤

📌 Вы можете пройти психологический тест, чтобы составить свой психологический портрет. 🕵️‍♀️
Бот будет использовать ваши данные в общении с вами и лучше понимать вас. &lt;b&gt;[скоро!] ✴🆕&lt;/b&gt;

📌 Ответьте на несколько простых вопросов. 📝
Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время."""]: ...

    @staticmethod
    def gender() -> Literal["""&lt;b&gt;🙋 Кто я - мужчина или женщина?&lt;/b&gt;

✅ Мне бы хотелось, чтобы меня не путали с тем, кем я не являюсь."""]: ...

    @staticmethod
    def grade() -> Literal["""&lt;b&gt;Как я оценил бы уровень своего эмоционального состояния?&lt;/b&gt;"""]: ...


class WinProfile:
    h: WinProfileH


class WinProfileH:
    @staticmethod
    def status() -> Literal["""&lt;b&gt;❤️‍🔥 Для меня сейчас важно:&lt;/b&gt;"""]: ...

    @staticmethod
    def grade() -> Literal["""&lt;b&gt;📶 Моё состояние:&lt;/b&gt;"""]: ...


class WinName:
    @staticmethod
    def __call__() -> Literal["""&lt;b&gt;🙋 Моё имя&lt;/b&gt;"""]: ...

    @staticmethod
    def txt() -> Literal["""✅ Приятно, если ко мне обращаются так, как мне это нравится 🤝."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;💁 Я ошибся:&lt;/b&gt;

✅ В имени не должно быть ничего лишнего:
цифры, знаки и т.п., 🤷"""]: ...


class WinAge:
    @staticmethod
    def h() -> Literal["""Мне"""]: ...

    @staticmethod
    def txt() -> Literal["""✅ В общении люди всегда учитывают возраст собеседника."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;💁 Я ошибся:&lt;/b&gt;

✅ Вряд ли мне меньше 5 или больше 150 лет,
или я укажу возраст чем-нибудь, кроме числа. 🤷"""]: ...


class WinStatus:
    @staticmethod
    def h() -> Literal["""Хочу рассказать, что для меня сейчас важнее всего: ‼"""]: ...

    @staticmethod
    def txt() -> Literal["""✅ В настоящее время и в ближайщем будущем - лично для меня и моего самочувствия,
✅ Какую проблему решаем,
✅ Что направляет мои мысли, мои эмоции, мои действия,
✅ Есть ли проблема, которая беспокоит меня больше всего,
✅ Как я чувствую себя в целом, как настроение,
✅ И ещё много чего."""]: ...

    @staticmethod
    def error() -> Literal["""&lt;b&gt;💁 Я ошибся:&lt;/b&gt;

✅ Если я что-то хочу рассказать, то вряд ли это будет пустой текст или только числа 🤷"""]: ...


class WinYesno:
    @staticmethod
    def name() -> Literal["""Точно изменить моё имя на"""]: ...

    @staticmethod
    def age() -> Literal["""Точно изменить кто я, мужчина или женщина, на"""]: ...


class Gpt:
    pmt: GptPmt


class GptPmt:
    psycholog: GptPmtPsycholog


class GptPmtPsycholog:
    finish: GptPmtPsychologFinish
    person: GptPmtPsychologPerson


class GptPmtPsychologFinish:
    @staticmethod
    def createreview() -> Literal["""Дайте развёрнутую характеристику моему психологическому состоянию по итогам всего нашего диалога, принимая во внимание все ваши знания из области психологии, психоанализа, конфликтологии, психиатрии, социальных наук, а также вашего общения с другими людьми. Выделите и сформулируйте конкретные проблемные вопросы так, чтобы вы могли продолжить наш разговор и обсудить со мной все эти вопросы в будущем. Не полагайтесь только на беседу в этот раз, а обязательно примите во внимание то, какой была ваша последняя оценка, с которой вы начали разговор со мной."""]: ...


class GptPmtPsychologPerson:
    name: GptPmtPsychologPersonName
    age: GptPmtPsychologPersonAge
    gender: GptPmtPsychologPersonGender

    @staticmethod
    def data() -> Literal["""Учитывайте следующие данные обо мне:"""]: ...

    @staticmethod
    def status() -> Literal["""В настоящее время особую важность для меня представляет следующее:"""]: ...

    @staticmethod
    def grade() -> Literal["""Примите во внимание следующую шкалу уровня моего психического и эмоционального состояния: по шкале от минус пяти до плюс пяти, то есть в цифрах: от -5 до +5. Состояние тем хуже, чем меньше число: отрицательне число характеризует негативное состояние и плохое самочувствие, ноль характеризует нейтральное состояние, положительное число характеризует позитивное состояние и хорошее самочувствие. Минимальное число минус пять характеризует крайнюю степень плохого психического здоровья, возможно глубокую депрессию, суециидальные мысли. Максимальное число плюс пять характеризует краунюю степень хорошего психического здоровья, сильный эмоциональный подъём, чувство радости и испытание высокого уровня чувства удовольствия. По такой шкале моё эмоциональное состояние оценивается числом"""]: ...

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


class Btn:
    getback: BtnGetback
    cancel: BtnCancel
    start: BtnStart
    psychology: BtnPsychology
    tests: BtnTests
    aboutme: BtnAboutme
    profile: BtnProfile
    gender: BtnGender

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
    def reset() -> Literal["""Вернуть ↪"""]: ...

    @staticmethod
    def save() -> Literal["""Сохранить 💾"""]: ...

    @staticmethod
    def ok() -> Literal["""Ok ☑️"""]: ...

    @staticmethod
    def yes() -> Literal["""Ok ✔"""]: ...

    @staticmethod
    def no() -> Literal["""Ok ✖"""]: ...


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
    def psychology() -> Literal["""Сеанс с психологом 🕵️‍♀️   ✴"""]: ...

    @staticmethod
    def tests() -> Literal["""Тесты 📝   ✴"""]: ...

    @staticmethod
    def aboutme() -> Literal["""О себе 👤   ✴"""]: ...


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
    def dotest() -> Literal["""Пройти тест 📝"""]: ...


class BtnAboutme:
    @staticmethod
    def profile() -> Literal["""Рссказать о себе 🙋"""]: ...


class BtnProfile:
    @staticmethod
    def name() -> Literal["""Имя 🙎"""]: ...

    @staticmethod
    def gender() -> Literal["""Пол 🙎"""]: ...

    @staticmethod
    def age() -> Literal["""Возраст 🙎"""]: ...

    @staticmethod
    def status() -> Literal["""Сейчас важно! ❤️‍🔥"""]: ...

    @staticmethod
    def grade() -> Literal["""Оценка состояния 📶"""]: ...


class BtnGender:
    @staticmethod
    def male() -> Literal["""М ♂"""]: ...

    @staticmethod
    def female() -> Literal["""Ж ♀"""]: ...

