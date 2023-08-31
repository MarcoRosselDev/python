from datetime import datetime
now = datetime.now()
print(now)                      # 2023-08-30 21:28:48.252618
day = now.day                   # 30
month = now.month               # 8
year = now.year                 # 2023
hour = now.hour                 # 21
minute = now.minute             # 28
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)                       # timestamp 1693445328.252618
print(f'{day}/{month}/{year}, {hour}:{minute}')     # 30/8/2023, 21:28