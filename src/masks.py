def get_mask_card_number(card_number: int | str) -> str:
    """Выводит маску карты"""
    if not card_number:
        return "Нет данных"
    elif len(str(card_number)) == 16:
        return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"
    else:
        return "Введён неверный формат данных"


def get_mask_account(card_number: int | str) -> str:
    """Выводит маску аккаунта"""
    if not card_number:
        return "Нет данных"
    elif len(str(card_number)) == 20:
        return f"**{str(card_number)[-4:]}"
    else:
        return "Введён неверный формат данных"

