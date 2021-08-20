import random
import string

s1=string.ascii_lowercase 
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
password_length=int(input("Enter your password length: "))

password=[]

password.extend(list(s1))
password.extend(list(s2))
password.extend(list(s3))
password.extend(list(s4))
random.shuffle(password)
print("YOUR PASSWORD IS:")
print("".join(password[0:password_length]))
