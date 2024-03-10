from datetime import datetime

date1 = datetime(year=2019, month=6, day=15, hour=20, minute=45, second=25)

year = date1.year
month = date1.month
day = date1.day
hour = date1.hour
minute = date1.minute
secons = date1.second

print(date1)
print(year)
print(month)
print(day)
print(hour)
print(minute)
print(secons)

now = datetime.now()
today = datetime.now().today()

print(now)
print(today)

date2_str = '2019-06-16 20:45:25'
date2 = datetime.strptime(date2_str, '%Y-%m-%d %H:%M:%S')

print(date2_str)
print(date2)

#######Operaciones

time_diff = date2 - date1

print('Diferencia de segundos:', time_diff.total_seconds())
print('Diferencia de minutos:', time_diff.total_seconds() / 60)

date1_seconds = date1.hour*3600 + date1.minute*60 + date1.second
print(date1_seconds)

date1_str = date1.strftime('%d-%m-%Y | %H:%M')
print(date1_str)



