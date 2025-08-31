#61.	Use datetime built-in module & show fulldate, time, day, month and year.
from datetime import date
from datetime import datetime
today=date.today()
print("Today's date is:",today)
now=datetime.now()
current_time=now.strftime("%H:%M:%S")
print("Time:",current_time)
print("Year:",today.year)
print("Month:",today.month)
print("Day:",today.day)
