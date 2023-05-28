from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    # Convert the date strings to datetime objects
    from_datetime = datetime.strptime(from_date, '%y-%m-%d')
    to_datetime = datetime.strptime(to_date, '%y-%m-%d')

    # Calculate the difference between the dates
    date_difference = abs((to_datetime - from_datetime).days)

    # Check if the date difference is less than the given difference
    if date_difference < difference:
        return True
    else:
        return False

# Example usage:
from_date = '21-05-01'
to_date = '21-05-15'
difference = 20
result = check_date_difference(from_date, to_date, difference)
print(result)


from_date = '21-05-01'
to_date = '21-05-29'
difference = 20
result = check_date_difference(from_date, to_date, difference)
print(result)