import string
import random
 
# Getting password length
length = int(input("Enter password length: "))

characterList = string.ascii_letters + string.digits + string.punctuation
 
password = []
 
for i in range(length):
   
    # Picking a random character from our 
    # character list
    randomchar = random.choice(characterList)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))
