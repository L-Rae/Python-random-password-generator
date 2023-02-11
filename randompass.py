
#import the random module 
import random 

#create a list of characters to choose from 
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"

#create an empty string to store the password 
password = "" 

#generate a random password with 8 characters 
for i in range(8): 
    password += random.choice(characters) 
    
#print the generated password 
print("Your new password is:", password)
