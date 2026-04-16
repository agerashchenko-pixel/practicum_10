A = int(input())
B = int(input())
N = int(input())

for i in range(1, N + 1):
    if i % A == 0 and i % B == 0:
        print(i)