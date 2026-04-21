from datetime import datetime


def calculate_total_seconds(date):
    """
    Calculate and print the total seconds passed since the start of the year.
    :param date: date string in format "%m/%d/%Y %H:%M:%S"
    :return: None
    """
    dt = datetime.strptime(date, "%m/%d/%Y %H:%M:%S")
    t = dt.timetuple()

    days_seconds = (t.tm_yday - 1) * 24 * 3600
    current_day_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second
    total_seconds = days_seconds + current_day_seconds

    print(total_seconds)


date_input = input()
calculate_total_seconds(date_input)
