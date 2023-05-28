from datetime import datetime, timedelta

def get_date_before(date, n):
    date_obj = datetime.strptime(date, '%y-%m-%d')
    date_before = date_obj - timedelta(days=n)
    date_before_str = date_before.strftime('%y-%m-%d')
    return date_before_str

date = '16-12-10'
n = 11
result = get_date_before(date, n)
print(result)
