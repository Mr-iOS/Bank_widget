from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_name: str) -> str:
    """Принимает строку, содержащую тип и номер карты или счета
    и возвращает строку с замаскированным номером"""
    if account_name:
        tmp_list = account_name.split()
    else:
        return "Введён неверный формат карты\\аккаунта"
    if len(tmp_list[-1]) == 16 and tmp_list[-1].isdigit():
        tmp_list[-1] = get_mask_card_number(int(tmp_list[-1]))
    elif len(tmp_list[-1]) == 20 and tmp_list[-1].isdigit():
        tmp_list[-1] = get_mask_account(int(tmp_list[-1]))
    else:
        return "Введён неверный формат карты\\аккаунта"
    return " ".join(tmp_list)


def get_date(date: str) -> str:
    """Форматирует дату в ДД.ММ.ГГГГ"""
    if date:
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
    return "Нет данных"


if __name__ == "__main__":
    test_list = [
        "Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305",
        "Счет 736541084301358743",
        "Счет 7365410843013587430t",
    ]
    for i in test_list:
        print(mask_account_card(i))
    print(get_date("2024-03-11T02:26:18.671407"))
