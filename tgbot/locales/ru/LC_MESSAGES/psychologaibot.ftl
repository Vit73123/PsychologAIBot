cmd-start = /start
cmd-start-description = Начать вё сначала

cmd-psychology = /psychology
cmd-psychology-description = Мой личный психолог

cmd-tests = /tests
cmd-tests-description = Тесты: психологические и не только

cmd-profile = /profile
cmd-profile-description = О себе: кто вы и как ваше самочувствие?

emoji-home = 🏠
emoji-pin = 📌
emoji-check = ✅
emoji-soon = ✴
emoji-new = 🆕
emoji-next = ▶
emoji-back = ◀
emoji-skip = ⏭
emoji-clear = 🧹
emoji-up = ⤴️
emoji-reset = ↪
emoji-save = 💾
emoji-ok = ☑️
emoji-yes = ✔
emoji-no = ✖
emoji-cancel = ✖

emoji-i-hi = 🙋
emoji-i-profile = 👤
emoji-i-am = 🙎
emoji-i-wrong = 💁
emoji-i-oh = 🤷
emoji-hands-handshake = 🤝
emoji-male = ♂
emoji-female = ♀

emoji-me-important = ❤️‍🔥
emoji-grade = 📶
emoji-psychologist-man = 🕵️‍♂️
emoji-psychologist-woman = 🕵️‍♀️
emoji-tests = 📝

txt-name-anonim = Новый пользователь

txt-aboutme-menothing = Я ещё ничего не рассказал о себе
txt-name-before-short = Меня зовут
txt-name-before-long-v1 = Моё имя
txt-name-before-long-v2 = Моё имя
txt-age-before-short = Мне
txt-age-before-long-v1 = Мой возраст
txt-age-before-long-v2 = Сколько мне лет
txt-age-after = лет
txt-gender-before-short = Я
txt-gender-before-long-v1 = Мой пол
txt-gender-before-long-v2 = Кто я - мужчина или женщина
txt-gender-male-short = М
txt-gender-female-short = Ж
txt-gender-male-long = мужчина
txt-gender-female-long = женщина

txt-yearsstring1 = год
txt-yearsstring2 = года
txt-yearsstring3 = лет

srv-name-checkname = ^[а-яА-ЯёЁ ]+

# Start ===========================================================================================

win-start = <b>Добро пожаловать в Бот психологической поддержки!</b>
    Общайтесь с Ботом анонимно или заполните профиль о себе, тогда Бот сможет подстроиться и лучше понимать вас.

    <b>Выбирайте:</b>
    { emoji-pin } <b>Сеанс с психологом</b> - поговорите с психологом, поделитесь своей <b>[скоро!] { emoji-soon }{ emoji-new }</b>
    { emoji-pin } <b>Тесты</b> - пройдите тесты и узнайте больше о себе <b>[скоро!] { emoji-soon }{ emoji-new }</b>
    { emoji-pin } <b>О себе</b> - добавьте информацию о себе, составьте свой психологический профиль <b>[скоро!] { emoji-soon }{ emoji-new }</b>

# Psychology ======================================================================================

win-psychology = <b>Мой личный психолог</b>

    { emoji-pin } Психолог пообщается с вами и постарается улучшить ваше психологическое самочувствие.

    Будьте искренни и доброжелательны.

# Tests ===========================================================================================

win-tests = <b>Тесты: психологические и не только</b> <b>[скоро!] { emoji-soon }{ emoji-new }</b>

    { emoji-pin } Пройдите психологический тест, чтобы лучше понять себя.

    Чем больше вы знаете о себе, тем проще вам и вашим окружающим понимать вас и общаться с вами.
    Знайте: все люди разные, и кем бы вы не хотели казаться самому себе, ваша природа останется той как она есть.
    Тест не даёт критической оценки: хорошо или плохо. Тест раскрывает вашу природу.

    В добрый путь к самопознанию!

# Abotme ==========================================================================================

win-aboutme = <b>О себе: кто вы и как ваше самочувствие?</b>

    { emoji-pin } Создайте свой профиль и добавьте данные о себе. { emoji-i-profile }

    { emoji-pin } Вы можете пройти психологический тест, чтобы составить свой психологический портрет. { emoji-psychologist-woman }
    Бот будет использовать ваши данные в общении с вами и лучше понимать вас. <b>[скоро!] { emoji-soon }{ emoji-new }</b>

    { emoji-pin } Ответьте на несколько простых вопросов. { emoji-tests }
    Вы можете создать статус: опишите своё текущее состояние или проблему, что является актуальным для вас в ближайшее время.

# Profile -----------------------------------------------------------------------------------------

# Имя, возраст, пол формируются в одной строке в коде диалога

win-profile-h-status = <b>{ emoji-me-important } Для меня сейчас важно:</b>

win-profile-h-grade = <b>{ emoji-grade } Моё состояние:</b>

# Name --------------------------------------------------------------------------------------------

win-name = <b>{ emoji-i-hi } { txt-name-before-long-v2 }</b>

win-name-txt = { emoji-check } Приятно, если ко мне обращаются так, как мне это нравится { emoji-hands-handshake }.

win-name-error = <b>{ emoji-i-wrong } Я ошибся:</b>

    { emoji-check } В имени не должно быть ничего лишнего:
    цифры, знаки и т.п., { emoji-i-oh }

# Age ---------------------------------------------------------------------------------------------

win-age = <b>{ txt-age-before-long-v2 }?</b>

    { emoji-check } В общении люди всегда учитывают возраст собеседника.

win-age-error = <b>{ emoji-i-wrong } Я ошибся:</b>

    { emoji-check } Вряд ли мне меньше 5 или больше 150 лет,
    или я укажу возраст чем-нибудь, кроме числа. { emoji-i-oh }

# Gender ------------------------------------------------------------------------------------------

win-gender = <b>{ emoji-i-hi } {txt-gender-before-long-v2}?</b>

    { emoji-check } Мне бы хотелось, чтобы меня не путали с тем, кем я не являюсь.

# Status ------------------------------------------------------------------------------------------

win-status = Хочу рассказать, что для меня сейчас важнее всего: ‼

    { emoji-check } В настоящее время и в ближайщем будущем - лично для меня и моего самочувствия,
    { emoji-check } Какую проблему решаем,
    { emoji-check } Что направляет мои мысли, мои эмоции, мои действия,
    { emoji-check } Есть ли проблема, которая беспокоит меня больше всего,
    { emoji-check } Как я чувствую себя в целом, как настроение,
    { emoji-check } И ещё много чего.

# Grade -------------------------------------------------------------------------------------------

win-grade = <b>Как я оценил бы уровень своего эмоционального состояния?</b>

# Yes/No Name -------------------------------------------------------------------------------------

win-yesno-name = Точно изменить моё имя на

# Yes/No Age --------------------------------------------------------------------------------------

win-yesno-age = Точно изменить сколько мне лет на

# Yes/No Gender -----------------------------------------------------------------------------------

win-yesno-age = Точно изменить кто я, мужчина или женщина, на

# GPT prompts =====================================================================================

gpt-pmt-psycholog-finish-createreview = Дайте развёрнутую характеристику моему психологическому состоянию по итогам всего нашего диалога, принимая во внимание все ваши знания из области психологии, психоанализа, конфликтологии, психиатрии, социальных наук, а также вашего общения с другими людьми. Выделите и сформулируйте конкретные проблемные вопросы так, чтобы вы могли продолжить наш разговор и обсудить со мной все эти вопросы в будущем. Не полагайтесь только на беседу в этот раз, а обязательно примите во внимание то, какой была ваша последняя оценка, с которой вы начали разговор со мной.

gpt-pmt-psycholog-person-data = Учитывайте следующие данные обо мне:
gpt-pmt-psycholog-person-name = меня зовут
gpt-pmt-psycholog-person-name-anoninm = я не хочу называть своего имени
gpt-pmt-psycholog-person-age = мой возраст
gpt-pmt-psycholog-person-age-anonim = мой возраст останется неизвестен
gpt-pmt-psycholog-person-gender = пол человека
gpt-pmt-psycholog-person-gender-anonim = мой пол останется неизвестен
gpt-pmt-psycholog-person-status = В настоящее время особую важность для меня представляет следующее:
gpt-pmt-psycholog-person-review = Ваши выводы из нашего последнего сеанса общения с вами:

# Buttons =========================================================================================

btn-next = Вперёд { emoji-next }
btn-back = Назад { emoji-back }
btn-home = Главное меню { emoji-home }
btn-getback = Назад { emoji-up }
btn-getback-home = Вернуться в главное меню { emoji-home }
btn-skip = Попустить { emoji-skip }
btn-clear = Сброс { emoji-clear }
btn-reset = Вернуть { emoji-reset }
btn-save = Сохранить { emoji-save }
btn-ok = Ok { emoji-ok }
btn-yes = Ok { emoji-yes }
btn-no = Ok { emoji-no }
btn-cancel = Отмена { emoji-cancel }
btn-cancel-getback = Отмена { emoji-up }

# Start -------------------------------------------------------------------------------------------

btn-start-psychology = Сеанс с психологом { emoji-psychologist-woman }
btn-start-tests = Тесты { emoji-tests }   { emoji-soon }
btn-start-aboutme = О себе { emoji-i-profile }   { emoji-soon }

# Psycholoty --------------------------------------------------------------------------------------

btn-psychology-appointment-start = Начать сеанс
btn-psychology-appointment-new = Новый сеанс
btn-psychology-appointment-follow = Продолжить сеанс
btn-psychology-appointment-stop = Звершить сеанс
btn-psychology-appointment-thankyou = Спасибо!

# Tests -------------------------------------------------------------------------------------------

btn-tests-start-choosetest = Выбрать тест
btn-tests-start-dotest = Пройти тест {emoji-tests}

# Aboutme -----------------------------------------------------------------------------------------

btn-aboutme-profile = Рссказать о себе { emoji-i-hi }

# Profile -----------------------------------------------------------------------------------------

btn-profile-name = Имя { emoji-i-am }
btn-profile-gender = Пол { emoji-i-am }
btn-profile-age = Возраст { emoji-i-am }
btn-profile-status = Сейчас важно! { emoji-me-important }
btn-profile-grade = Оценка состояния { emoji-grade }

# Gender ------------------------------------------------------------------------------------------

btn-gender-male = {txt-gender-male-short} { emoji-male }
btn-gender-female = {txt-gender-female-short} { emoji-female }
