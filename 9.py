from datetime import datetime

date = input()
dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
t = dt.timetuple()

days_seconds = (t.tm_yday - 1) * 24 * 3600
current_day_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second
total_seconds = days_seconds + current_day_seconds

print(total_seconds)
