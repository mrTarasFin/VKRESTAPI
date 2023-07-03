from config_db import session_db
from model import DataRequest
from config_db import session_db
from dataclasses import dataclass, field
from datetime import datetime


# Этот модуль использовал для работы с БД
@dataclass
class ParamRequest:
    '''
    Класс структуры данных, передаваемый для запроса в базу данных
    '''
    date: datetime
    field_search: str
    user_id: str
    groups: list = field(default_factory=list)

    def __repr__(self):
        return f'{self.__dict__}'


def get_data_db() -> dict:
    '''
    Функция получает список групп в базе данных
    :return: словарю date=list - список групп
    '''
    get_data = session_db.query(DataRequest).all()
    data = [f'{item.date}: {item.groups}' for item in get_data]
    return data


def add_data_db(parameters: ParamRequest) -> None:
    '''
    Функция добавляет данные в базу данных
    :param parameters: класс параметров для добавления
    '''
    try:
        add_data = DataRequest(date=parameters.date,
                               field_search=parameters.field_search,
                               id_user=parameters.user_id,
                               groups=parameters.groups,
                               )
        session_db.add(add_data)
        session_db.commit()
        session_db.close()
    except Exception:
        session_db.rollback()