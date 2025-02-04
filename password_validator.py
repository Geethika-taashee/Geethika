#import re
#def validate_password(password):
#    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#    if re.fullmatch(pattern, password):
#        return "Password is valid"
#    else:
#        return "Password is notvalid"
#password=input("Enter a password:")
#print(validate_password(password))



#def validate():
#        password = input("Enter a password:")
#        if len(password) < 8:
#            print("password is invalid")
#        else:
#            print("password is valid")
#validate()



def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_characters = "@$!%*?&"
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "password is valid"
    else:
        return "password is  invalid"
password=input("Enter a password:")
print(validate_password(password))
    
