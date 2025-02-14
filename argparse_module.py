#implement argparse to create a command-line interface
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("num1",help="first number")
# parser.add_argument("num2",help="second number")
# parser.add_argument("operation",help="operation")
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
# n1=int(args.num1)
# n2=int(args.num2)
# result=n1+n2
# print("the result is:",result)


#simple caluclator program using argparse
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("num1",help="first number")
# parser.add_argument("num2",help="second number")
# parser.add_argument("operation",help="operation")
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)
# print(args.operation)
# n1=int(args.num1)
# n2=int(args.num2)
# if args.operation == "add":
#     result=n1+n2
#     print("The result is :",result)
# elif args.operation == "sub":
#     result=n1-n2
# elif args.operation == "mul":
#     result=n1*n2
# elif args.operation == "div":
#     result=n1/n2
# else:
#     print("unmatched arguments")
# print("The result is:",result)


#sum of command-lines
# import argparse
# parser=argparse.ArgumentParser(description='process some integer:')
# parser.add_argument('integer',metavar='N',type=int,nargs='+',help='an integer for the accumulator')
# parser.add_argument(dest='accumulate',action='store_const',const=sum,help='sum of integer')
# args=parser.parse_args()
# print(args.accumulate(args.integer))


#arange integer input in ascending order
# import argparse
# parser=argparse.ArgumentParser(description='sort some integer')
# parser.add_argument('integers',metavar='N',type=int,nargs='+',help='an integer for the accumulator')
# parser.add_argument(dest='accumulate',action='store_const',const=sorted,help='arranges the integers in accending order')
# args=parser.parse_args()
# print(args.accumulate(args.integers))


#average of entered command line numerical arguments
import argparse
parser=argparse.ArgumentParser(description='sort some integer')
parser.add_argument('integer',metavar='N',type=int,nargs='+',help='an integer for the accumulator')
parser.add_argument('sum',action='store_const',const=sum)
parser.add_argument('len',action='store_const',const=len)
args=parser.parse_args()
add=args.sum(args.integer)
length=args.len(args.integer)
average=add/length
print(average)