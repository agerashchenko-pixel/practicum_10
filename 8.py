from datetime import datetime


def format_date(date):
    """
    Convert date string from one format to another and print it.
    :param date: date string in format "%m/%d/%Y %H:%M:%S"
    :return: None
    """
    try:
        dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
        print(dt.strftime("%d.%m.%y %I:%M:%S %p"))
    except ValueError:
        print("Неверная дата")


date = input()
format_date(date)
