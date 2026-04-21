def print_simple_numbers(N):
    """
    Find and print all prime numbers from 1 to N.
    :param N: the upper limit for checking primes
    :return: None
    """
    for num in range(1, N + 1):
        if num < 2:
            continue

        simple = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                simple = False
                break

        if simple:
            print(num)


N = int(input())
print_simple_numbers(N)
