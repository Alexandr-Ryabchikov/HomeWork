from src.widget import mask_account_card, get_date


user_input = input(str("Введите номер карты или счета: "))
print(mask_account_card(user_input))
print(get_date("2024-03-11T02:26:18.671407"))
