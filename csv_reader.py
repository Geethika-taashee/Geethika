#csv.reader()
# import csv
# with open('people.csv','r')as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#csv.DictReader()
import csv
with open('people.csv','r')as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
