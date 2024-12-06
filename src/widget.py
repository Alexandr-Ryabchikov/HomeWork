from typing import Union
from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_name: Union[str]) -> str:
    '''Функция масок банковских карт и счетов'''

    type_card = card_name.rpartition(" ")[0]
    card_number = card_name.rpartition(" ")[-1]
    if len(card_number) > 16:
        return f"{type_card} {get_mask_account(card_number)}"
    elif len(card_number) == 16:
        return f"{type_card} {get_mask_card_number(card_number)}"
    else:
        return "Неверное значение"



def get_date(data_string: Union[int]) -> str:
    '''Возвращает формат даты в виде ДД.ММ.ГГГГ'''

    return f"{str(data_string[8:10])}.{str(data_string[5:7])}.{str(data_string[:4])}"
