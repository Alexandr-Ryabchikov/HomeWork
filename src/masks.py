from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковской карты"""

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Функция маскировки номера банковского счета"""

    return f"**{account_number[-4:]}"
