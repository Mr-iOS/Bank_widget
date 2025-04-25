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


if __name__ == "__main__":
    test_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print([i["state"] for i in test_list])
    print("EXECUTED" in [i["state"] for i in test_list])
    print(filter_by_state(test_list, "ANY"))
    print(filter_by_state(test_list))
    print(filter_by_state(test_list, "CANCELED"))
    print("-" * 150)
    print(sort_by_date(test_list))
    print(sort_by_date(test_list, False))
