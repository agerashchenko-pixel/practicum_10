def print_message(message):
    """
    Print the message or its first 160 characters if the length exceeds the limit.
    :param message: the original string to be checked
    :return: None
    """
    if len(message) > 160:
        print(message[:160])
    else:
        print(message)


message = input()
print_message(message)
