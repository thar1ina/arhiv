import datetime
from datetime import date
from datetime import time
from datetime import datetime



# yesterday = datetime.date(2024, 8, 9)
# print(yesterday)
#
# yesterday1 = datetime.date(2023, 12, 13)
# print(yesterday1)



# today = date.today()
# print(today)
# print("{}/{}/{}".format(today.day - 9, today.month - 8, 2024 - today.year))

# current_time = time()
# print(current_time)

# current_time = time(00, 34)
# print(current_time)

# deadline = datetime(2023, 12, 14, 2,5,00)
# print(deadline)

# yesterday = datetime.date(2023,12, 12)
# print(yesterday)

# import datetime
#
# while True:
#     today = datetime()
#     brz = datetime.date(2024, 8, 9)
#     if today < brz:
#
# s = today.month - brz.month
# c = today.day - brz.day
# v = today.Year - brz.Year

# print(y%/m%/%d)


import datetime
# from datetime import date
# from datetime import time
# from datetime import datetime
# from datetime import datetime
# import datetime
# while True:
#     date = date.today()
#     b = datetime.date(2005, 8, 9)
#
#     new_date = date - datetime.timedelta(minutes=1)
#
#     print(new_date)

import datetime
from datetime import date
from datetime import time
from datetime import datetime
# from datetime import datetime
# open = datetime.strptime('09.08.2024 9:00:00', '%d.%m.%Y %H:%M:%S')
# now = datetime.now()
# a = now.day - open.day
# b = now.month - open.month
# c = now.year
# print(c, b, a)


# from datetime import datetime
# while True:
#     open = datetime.strptime('09.08.2024 9:00:00', '%d.%m.%Y %H:%M:%S')
#     now = datetime.now()
#     a = now.day - open.day
#     b = now.month - open.month
#     c = now.year
#     x = open - datetime.timedelta(second=1)
#     print(x)


# import time
#
#
# d = 365 * 24 * 60 * 60
#
#
# start_time = time.time()
#
# while True:
#
#     r = d - (time.time() - start_time)
#
#     print(r)
#
#     time.sleep(1)
#
#
#     if r <= 0:
#         break
#
# print("Таймер завершен.")


import datetime
import time


t_time = datetime.datetime.now() + datetime.timedelta(days=365)

while True:
    r_time = t_time - datetime.datetime.now()

    if r_time.total_seconds() <= 0:
        print("Время вышло!")
        break

    print("\rОсталось {} секунд".format(int(r_time.total_seconds())), end="")

    time.sleep(1)