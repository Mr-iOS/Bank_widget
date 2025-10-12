from src.masks import get_mask_card_number, get_mask_account


if __name__ == "__main__":
    account = "73654108430135874305"
    print(get_mask_account(account))
    card = "7000792289606361"
    print(get_mask_card_number(card))
