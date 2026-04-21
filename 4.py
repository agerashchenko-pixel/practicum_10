def make_payment(P):
    """
    Check if the payment amount is within the allowed range and print the result.
    :param P: the payment amount (string or number)
    :return: None
    """
    try:
        price = float(P)
        if 20 <= price <= 1000:
            print("Успех")
        else:
            print("Повторить попытку")
    except ValueError:
        print("Повторить попытку")


payment_input = input()
make_payment(payment_input)
