try:
    user_input=int(input("Enter a number:"))
    result=2*user_input
    print(f"Twice the input is: {result}")
except ValueError:
    print("Invalid input! please enter a valid integer.")
