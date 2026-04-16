from datetime import datetime

date = input()

try:
    dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
    print(dt.strftime("%d.%m.%y %I:%M:%S %p"))
except:
    print("Неверная дата")
