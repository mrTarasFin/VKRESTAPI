import os
import vk_api


def write_token_env() -> object:
    '''
    Функция записывает access_token в переменную окружения
    :return: сессию для запросов api к серверу vk
    '''
    try:
        os.environ['ACCESS_TOKEN']
    except Exception:
        os.environ.setdefault('ACCESS_TOKEN', input("Enter your access_token from VK: "))
        session_vk = vk_api.VkApi(token=os.environ['ACCESS_TOKEN'])
    return session_vk
