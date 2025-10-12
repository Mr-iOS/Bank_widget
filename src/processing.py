def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict] | str:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    if state in [i["state"] for i in list_of_dicts]:
        return [i for i in list_of_dicts if i["state"] == state]
    elif state not in [i["state"] for i in list_of_dicts]:
        return "Состояния нет в списке"
    return "Нет данных"


def sort_by_date(list_of_dicts: list[dict], is_reverse: bool = True) -> list[dict] | str:
    """Функция возвращает новый список, отсортированный по дате"""
    if list_of_dicts:
        return sorted(list_of_dicts, key=lambda x: x["date"], reverse=is_reverse)
    return "Нет данных"
