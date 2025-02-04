#x=int(input("Enter the starting number (x):"))
#y=int(input("Enter the ending number (y):"))
#total_sum=sum(ranges(x,y+1))
#print(f"the sum of numbers from {x} to {y} is: {total_sum}")


#x=int(input("Enter the starting number (x):"))
#y=int(input("Enter the ending number (y):"))
#if x>y:
#    x,y=y,x
#n=y-x+1
#sum_of_numbers=(n*(x+y))//2
#print(f"sum of numbers from {x} to {y} is: {sum_of_numbers}")



x=int(input("Enter the starting number (x):"))
y=int(input("Enter the ending number (y):"))
# if x>y:
#     x,y=y,x
# sum_of_numbers=0
# current_numbers=x
# for _ in "*" *(y-x+1):
#     sum_of_numbers += current_numbers
#     current_numbers += 1
# print(f"sum of numbers from {x} to {y} is: {sum_of_numbers}")

# sum_of_numbers = 0

# for i in range(x, y+1):
#     sum_of_numbers += i
# print(sum_of_numbers)

sum_of_numbers = 0
n = 0

while True:
    if n >= x and n <= y:
        sum_of_numbers += n
    elif n > y:
        break
    n += 1
print(sum_of_numbers)