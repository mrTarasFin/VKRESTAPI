# Тестовое задание

## Описание

* Парсер api с сервер соцальной сети VK.
* Запрашивает по подстроке название группы
* Проверяет ваших друзей состоящих в найденных группах
* Записывает данные в базу группы, в которых состоит пользователь
* Выгружает данные групп по всем запросам

## Технологии

* Python
* Библиотеки vk_api, sqlalchemy
* Данные сохраняются в БД MySQL

## Запуск проекта

1. Необходимо клонировать репозиторий с github в Вашу IDE:
    `git clone https://github.com/mrTarasFin/VKRESTAPI.git`

2. Скачать необходимые библиотеки

    `pip install -r requiremets.txt`

3. Для запуска использовать команды

    `python main.py` или запустить из IDE `main.py`