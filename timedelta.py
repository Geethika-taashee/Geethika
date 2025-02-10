#difference between two dates and times
# from datetime import datetime, date
# t1=date(year=2025,month=2,day=10)
# t2=date(year=2024,month=11,day=12)
# t3=t1-t2
# print("t3=",t3)
# t4=datetime(year=2025,month=6,day=22)
# t5=datetime(year=2024,month=11,day=12)
# t6=t4-t5
# print("t6=",t6)
# print("type of t3=",type(t3))
# print("type of t6=",type(t6))


#difference between two timedelta
from datetime import timedelta
t1=timedelta(weeks=4, days=6, hours=12, seconds=10)
t2=timedelta(days=2, hours=12, minutes=36, seconds=33)
t3=t1-t2
print("t3=",t3)