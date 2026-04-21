def print_fibonacci(N):
    last_num = 1
    bl_num = 1

    for i in range(N):
        print(bl_num)
        incr_bl_num = bl_num
        bl_num = last_num
        last_num = incr_bl_num + last_num


N = int(input())
print_fibonacci(N)
