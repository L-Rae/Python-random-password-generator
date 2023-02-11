import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"

password = ""

for i in range(8): 
    password += random.choice(characters) 
    
print("Your new password is:", password)    
