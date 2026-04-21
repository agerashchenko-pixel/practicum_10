from datetime import datetime


def format_date(date):
    try:
        dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
        print(dt.strftime("%d.%m.%y %I:%M:%S %p"))
    except ValueError:
        print("Неверная дата")


date = input()
format_date(date)
