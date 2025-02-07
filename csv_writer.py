#csv.writer()
# import csv
# data =[
    # ['Name','Branch','Year'],
    # ['varun','IT',4],
    # ['siri','CSE',2],
    # ['Arjun','AIML',1],
    # ['Divya','IOT',3]

# ]
# with open('university_records.csv',mode='w',newline='') as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerows(data)


#csv.DictWriter():
# import csv
# data = [
#     {'name':'varun','branch':'IT','year':4},
#     {'name':'siri','branch':'CSE','year':2},
#     {'name':'arjun','branch':'AIML','year':1},
#     {'name':'divya','branch':'IOT','year':3}
# ]
# with open('university_records.csv',mode='w',newline='') as csvfile:
#     fieldnames=['name','branch','year']
#     writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(data)


#email_records.csv()
import csv
data = [
    ['Name','email'],
    ['Nikhil', 'nikhil.gfg@gmail.com'],
    ['Sanchit', 'sanchit.gfg@gmail.com'],
    ['Aditya', 'aditya.gfg@gmail.com'],
    ['Sagar', 'sagar.gfg@gmail.com'],
    ['Prateek', 'prateek.gfg@gmail.com']
]
with open('email_records.csv','w') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerows(data)