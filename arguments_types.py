#positional arguments in command-line interface
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('num',help='Enter number to square of it.',type=int)
# args=parser.parse_args()
# print(args.num**2)


#optional arguments in command-line interface in this we will use the '-'single dash or '--'double dash
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("--num1",help="first number")
# parser.add_argument("--num2",help="second number")
# parser.add_argument("--operation",help="operation")
# args=parser.parse_args()
# print(args.num1)
# print(args.num2)                    # in this code we will get none because we did not pas any arguments
# print(args.operation)
# n1=int(args.num1)
# n2=int(args.num2)
# if args.operation == "add":
#     result=n1+n2
# elif args.operation == "sub":
#     result=n1-n2
# elif args.operation == "mul":
#     result=n1*n2
# elif args.operation == "div":
#     result=n1/n2
# else:
#     print("unmatched arguments")
# print("The result is:",result)


#positional arguments by default value
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("example",default='hello how are you')
# args=parser.parse_args()
# if args.example =='hello':
#     print("Welcome to python")
# else:
#     print("unmatched")


#using short names for optional arguments
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('-tut','--tutorial',help='best tutorial')
# parser.add_argument('-w','--writer',help='technical content')
# args=parser.parse_args()
# if args.tutorial == 'hello':
#     print("congratulation! you made it")
# if args.writer == 'geethika':
#     print("technical writer")


#combining positional and optional arguments
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument('tutorial',help='best tutorial')   #positional arguments
# parser.add_argument('-w','--writer',help='technical content')
# args=parser.parse_args()
# if args.tutorial == 'hello':
#     print("you made it")
# if args.writer == 'geethika':
#     print("technical writer")