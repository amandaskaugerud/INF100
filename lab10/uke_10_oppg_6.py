from datetime import datetime, timedelta

def first_friday_13th_after(date):
    while date != 0:
        date = date + timedelta(days=1)
        if date.day == 13 and date.weekday() == 4:
            return date

