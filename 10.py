a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

if a > b:
    a, b = b, a

symbols = "13489"

for num in range(a, b + 1):
    num_str = str(num)

    is_good = True

    for digit in num_str:
        if digit not in symbols:
            is_good = False
            break

    if is_good:
        print(num)