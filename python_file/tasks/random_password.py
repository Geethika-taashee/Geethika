import random
import string
length=int(input("Enter password length:"))
password=''.join(random.choices(string.ascii_letters+string.digits+string.punctuation,k=length))
print("Generated password:",password)