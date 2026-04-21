def print_common_multiples(A, B, N):
    """
    Print all common multiples of A and B up to N.
    :param A: first divisor
    :param B: second divisor
    :param N: upper limit for checking
    :return: None
    """
    for i in range(1, N + 1):
        if i % A == 0 and i % B == 0:
            print(i)


A = int(input())
B = int(input())
N = int(input())
print_common_multiples(A, B, N)
