from datetime import datetime, timezone, timedelta

t = datetime.now()
t_z = datetime.now(timezone.utc)

tomm = t_z + timedelta(days = 1)
print(tomm.strftime('%d-%m-%Y %H-%M-%s'))

user_date = input('Enter date in YYYY-MM-DD format :: ')
print(datetime.strptime(user_date, '%Y-%m-%d'))