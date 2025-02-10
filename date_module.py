# from datetime import date
# my_date=(2025,2,10)
# print("Date passed as arguments is:",my_date)

#get the current date
# from datetime import date
# today = date.today()
# print(today)

#get today year,month,date
# from datetime import date
# today = date.today()
# print("current year:",today.year)
# print("current month:",today.month)
# print("current day:",today.day)

#get date from timestamp
# from datetime import datetime
# date_time=datetime.fromtimestamp( 1739179644)
# print("datetime from timestamp:",date_time)

#convert date to string
# from datetime import date
# today=date.today()
# str=date.isoformat(today)
# print("string repesentation:",str)
# print(type(str))

#min max representable date
# from datetime import date
# mindate=date.min
# print("min date supported",mindate)
# maxdate=date.max
# print("max date supported",maxdate)

#attributes of datetime 
import datetime
print(dir(datetime))