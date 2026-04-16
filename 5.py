amount = int(input())

if amount == 5 or amount == 10:
    total = amount
    print(total)
elif amount == 25:
    total = amount + 3
    print(total)
elif amount == 50:
    total = amount + 8
    print(total)
elif amount == 100:
    total = amount + 20
    print(total)
else:
    print("Недопустимое значение")
