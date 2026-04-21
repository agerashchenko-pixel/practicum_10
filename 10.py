def print_filtered_numbers(a, b):
    """
    Check numbers in range and print those consisting only of 1, 3, 4, 8, 9.
    :param a: start of the range
    :param b: end of the range
    :return: None
    """
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


a = int(input())
b = int(input())
print_filtered_numbers(a, b)
