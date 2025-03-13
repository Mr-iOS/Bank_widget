def get_mask_card_number(card_number: int) -> str:
    """Выводит маску карты"""
    return f"{str(card_number)[:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


def get_mask_account(card_number: int) -> str:
    """Выводит маску аккаунта"""
    return f"**{str(card_number)[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(1234567890123451))
    print(get_mask_account(12345678901234567890))
