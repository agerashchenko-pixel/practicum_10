message = input()

if len(message) > 160:
    print(message[:160])
else:
    print(message)
