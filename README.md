# Бот "Психологическая поддержка"

Телеграм-бот для оказания психологической поддержки пользователям.

Комфортная атмосфера и положительный эмоциональный фон благодаря приятным вступительным сообщениям в диалогах с иллюстрациями;

## Технологии:

* Настраиваемый чат-бот с ChatGPT на базе библиотеки openai
* Архитектура бэкенда MVC
* База данных SQLite
* SQLAlchemy Core и ORM
* Интерактивные диалоги на платформе aiogram_dialog
* Интернационализация fluent на базе библиотеки fulentogramm

## Особенности работы:
Автоматическая регистрация пользователя и сохранение в базе данных при первом запуске бота.  

Пользователь использует бот анонимно или добавляет данные о себе, которые учитывается в диалогах бота и в сеансе с ChatGPT.  

Кроме основных данных пользователь может описать своё психологическое состояние и проставить ему оценку.  

Заполнение профиля пользователя в интерактивных диалоговых окнах с кнопками выбора, радио-кнопками, валидацией данных и другими инструментами.

Текстовые сообщения бота формируются в "свободном стиле" из соответствующих реплик в словаре fluent.  

Бот сохраняет всю историю взаимодействия пользователя с ботом, включая его сеансы с ChatGPT, психологические состояния, описанные пользователем.

История сеансов и психологического состояния пользователя учитывается в сеансах с ChatGPT.

## Чат-бот "Сеанс с психологом"

Настраиваемый чат с ChatGPT, учитывающий все характеристики пользователя и выбирающий оптимальную форму общения:
* настраивается с помощью начального промпта, который  можно выбрать из коллекции категорий в конфигуарции бота;
* общается с пользователем персонифицированно, если пользователь не возражает;
* учитывает все характеристики пользователя и изменение его состояния со слова пользователя и по итогам сеансов с ChatGPT;
* ChatGPT даёт итоговую оценку психологическому состоянию пользователя после каждого сеанса;
* все оценки ChatGPT сохраняются и учитываются в последующих сеансах
