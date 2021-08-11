from datetime import datetime
import jdatetime
from persiantools import digits

def persian_time(date_time):
    created_at = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%S.%f%z')
    jalali_date = jdatetime.date.fromgregorian(day=created_at.day,month=created_at.month,year=created_at.year)
    formated_date = "{}/{}/{} - {}:{}".format(jalali_date.year, jalali_date.month, jalali_date.day, created_at.hour, f'{created_at.minute:02}')
    return digits.en_to_fa(formated_date)
