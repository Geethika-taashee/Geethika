#date time object representing date time
# from datetime import datetime
# a=datetime(2025,2,10)
# print(a)
# a=datetime(2025,2,10,15,35,20)
# print(a)

#get year,month,hour,minute,timestamp
# from datetime import datetime
# Time=datetime(2025,2,2,2,2)
# print("current year:",Time.year)
# print("current month:",Time.month)
# print("current hour:",Time.hour)
# print("current minute:",Time.minute)
# print("current timestamp:",Time.timestamp())

#current date and time
# from datetime import datetime
# today=datetime.now()
# print("current date and time is:",today)

#convert datetime to string
# from datetime import datetime
# now=datetime.now()
# string=datetime.isoformat(now)
# print(string)
# print(type(string))

#format datetime by strftime
# from datetime import datetime as dt
# now=dt.now()
# print("without formating:",now)
# s = now.strftime("%a %m %Y")
# print("datetime:",s)

#format datetime by strptime
from datetime import datetime
time_date=["10/2/25 16:14:10.025"]
format_date="%d/%m/%y %H:%M:%S.%f"
for i in time_date:
    print(datetime.strptime(i,format_date))