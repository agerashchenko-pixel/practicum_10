def make_payment(P):
    try:
        price = float(P)
        if 20 <= price <= 1000:
            print("Успех")
        else:
            print("Повторить попытку")
    except ValueError:
        print("Повторить попытку")



