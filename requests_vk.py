from typing import List
from dataclasses import dataclass, field
from main import ParamRequest


def search_groups(session: object, field_search: str, limit: str) -> list:
    '''
    Функция осуществляет поиск по подстроке всех групп(сообществ)
    :param session: параметр сессии для api запроса
    :param field_search: подстрока поиска
    :param limit: лимит на поиск (лимит ограничен разработчиками vk api
    :return: возвращает список найденных групп с type=group
    '''
    flag = True
    while flag:

        if limit.isdigit() and (0 < int(limit) <= 200):
            res = session.method("search.getHints", {"q": field_search,
                                                     "limit": limit,
                                                     "search_global": 1,
                                                     }
                                 )
            flag = False
        else:
            print("Значение лимита не должно быть больше 200 и меньше 0, а также только числа: ")
            limit = input('Введите повторно лимит поиска: ')

    list_id_groups = [item['group'].get('id') for item in res['items'] if item.get('group')]

    return list_id_groups


def list_friends_user(session: object, id_user: str) -> dict:
    '''
    Функция возвращает список друзей пользователя, исключение status=deactivate,delete
    :param session: параметр сессии для api запроса
    :param id_user: id пользователя
    :return: список id друзей пользователя
    '''
    get_id_friends = session.method("friends.get", {"user_id": id_user,
                                                    "fields": "nickname"}
                                    )
    dict_groups = {}
    for item in get_id_friends['items']:

        if 'deactivated' not in item.keys():
            get_groups_friend = session.method("groups.get", {"user_id": item['id']})
            dict_groups[item['id']] = get_groups_friend['items']

    return dict_groups


def all_groups_user(session: object, id_user: str) -> list:
    '''
    Функция возвращает список групп пользователя
    :param session: параметр сессии для api запроса
    :param id_user: id пользователя
    :return: список id групп пользователя
    '''
    user_groups = session.method("groups.get", {"user_id": id_user})
    result = user_groups['items']
    return result


def share_groups_friends(list_seach_groups: list, groups_friends: dict) -> dict:
    '''
    Функция сверяет id групп из функции search_groups() с id групп друзей пользователя.
    Сравнивает совпадения с глобальным поиском
    :param list_seach_groups: список id групп глобального поиска
    :param groups_friends: id групп друзей
    :return: возвращает словарь friend=list - список групп
    '''
    common_dict = {}
    for item in groups_friends.items():
        share_list = list(set(list_seach_groups) & set(item[1]))
        common_dict[item[0]] = share_list
    return common_dict


def share_groups_user(list_seach_groups: list, groups_user: list) -> list:
    '''
    Функция сверяет id групп пользователя с глобальным поиском и возвращает совпадения
    :param list_seach_groups: id групп глобального поиска
    :param groups_user: id групп пользователя
    :return: список id групп
    '''
    share_list_user = list(set(list_seach_groups) & set(groups_user))
    return share_list_user
