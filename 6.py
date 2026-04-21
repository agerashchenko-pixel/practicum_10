def print_message(message):
    if len(message) > 160:
        print(message[:160])
    else:
        print(message)


message = input()
print_message(message)
