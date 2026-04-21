def calculate_price(price, card, day):
    """
    Calculate the final price with cumulative discounts and print it.
    :param price: initial cost
    :param card: 'yes' if customer has a card, otherwise 'no'
    :param day: 'holiday' if it is a holiday, otherwise 'workday'
    :return: None
    """
    discount = 0

    if 15000 > price >= 5000:
        discount = 3
    elif 20000 > price >= 15000:
        discount = 5
    elif 30000 > price >= 20000:
        discount = 7
    elif price > 30000:
        discount = 10

    if card == 'yes':
        discount += 5

    if day == 'holiday':
        discount += 3

    if discount > 15:
        discount = 15

    final_price = price * (1 - (discount / 100))
    print(final_price)


price = float(input())
card = input()
day = input()
calculate_price(price, card, day)
