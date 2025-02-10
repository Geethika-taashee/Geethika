#time.gmtime-----> it represents the GMT(Greenwhich mean time)
import time
print(time.gmtime(0))


#time.time()------>it returns the current time in seconds since epoch
import time
curr=time.time()        
print("current time in seconds since epoch =", curr)


#time.ctime()------>returns 24 character time string but takes seconds it print thee cuurent time
import time
curr=time.ctime(1739164560.5527217)
print("current time =", curr)


#time.sleep()------>execution can be delayed by using this method
import time
for i in range(4):
    time.sleep(1)
    print(i)


#time.localtime()------>return the struct_time object in local time
import time
obj=time.localtime(1739165482.7641547)
print(obj)


#time.mktime()------>inverse function of time.localtime()
import time
obj1=time.gmtime(1739165482.7641547)
time_sec=time.mktime(obj1)
print("local time(in seconds):",time_sec)


#time.gmtime()----->convert a time expressed in deconds since the epoch to a time.struct_time
# import time
# obj = time.gmtime(1739165482.7641547)
# print(obj)

import time
curr=time.time()
obj = time.gmtime(curr)
print(obj)

#time.strftime()------->convert a tuple or struct_time
from time import gmtime , strftime
s=strftime("%a, %d %b %Y %H:%M:%S", gmtime(1739165482.7641547))
print(s)

#time.asctime()----->used to convert a tuple or a time.struct_time object representing a time 
# as returned by time.gmtime() or time.localtime() method to a string
import time
obj=time.gmtime(1739165482.7641547)  #or time.localtime()
time_str=time.asctime(obj)
print(time_str)

#time.strptime()----->converts the string representation time to struct_time
import time
string="Mon, 10 Feb 2025 05:31:22"
obj=time.strptime(string,"%a, %d %b %Y %H:%M:%S")
print(obj)
