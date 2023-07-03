import vk_api
from config import write_token_env
from requests_vk import *
from config_db import engine, Base
from dataclasses import dataclass, field
from datetime import datetime
from controller import add_data_db, get_data_db, ParamRequest


def main():
    '''
    Оснавная функция для запуска скрипта
    '''
    SEARCH_FIELD = input("Введите подстроку поиска сообщества: ")
    LIMIT = input("Введите лимит поиска сообществ, не более 200: ")
    USER_ID = input("Введите id пользователя: ")
    try:
        engine.connect()
        Base.metadata.create_all(engine)
        session = write_token_env()
        a = search_groups(session, SEARCH_FIELD, LIMIT)
        b = all_groups_user(session, USER_ID)
        list_friends_user(session, USER_ID)
        data_add_db = ParamRequest(date=datetime.now(),
                                   field_search=SEARCH_FIELD,
                                   user_id=USER_ID,
                                   groups=str(share_groups_user(a, b)),
                                   )
        add_data_db(data_add_db)
        get_data_db()

    except Exception as ex:
        print(f'ERROR: {ex}')
    except Exception as ex_db:
        print(f'ERROR DB: {ex_db}')


if __name__ == '__main__':
    main()
