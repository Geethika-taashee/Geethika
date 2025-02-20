#time object representing time 
# from datetime import time
# my_time=time(15,13,25)
# print("Entered the time:",my_time)
# my_time=time(minute=12)
# print("\ntime with one arguments:",my_time)
# my_time=time()
# print("\ntime without arguments:",my_time)

#get hrs, minutes,seconds and microseconds
# from datetime import time
# Time=time(12,20,35,10000)
# print("current hour:",Time.hour)
# print("current minute:",Time.minute)
# print("current second:",Time.second)
# print("current microsecond:",Time.microsecond)

#convert time object to string
from datetime import time
Time=time(15,37,45)
str=Time.isoformat()
print("string representaion:",str)
print(type(str))