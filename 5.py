def calculate_card_bonus(amount):
    """
    Calculate the total monetary value of a phone card including bonuses.
    :param amount: the cost of the card ($5, $10, $25, $50, $100)
    :return: total value with bonus or None if the amount is invalid
    """
    if amount == 5 or amount == 10:
        total = amount
        return total
    elif amount == 25:
        total = amount + 3
        return total
    elif amount == 50:
        total = amount + 8
        return total
    elif amount == 100:
        total = amount + 20
        return total
    else:
        return None


amount_input = int(input())
result = calculate_card_bonus(amount_input)

if result is not None:
    print(result)
else:
    print("Недопустимое значение")
