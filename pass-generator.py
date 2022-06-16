import random

#CREATING ALL TYPES VARIABLES#
lower_case = "abcdefghijklmnñopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
num = "0123456789"
specialChar = "|@#~€*!·$%/\()ª"

#Put all the variables together#
Use_for = lower_case + upper_case + num + specialChar

#Indicate the length of the password#
length_for_pass = 8;

#Creating the pass#
password = "".join(random.sample(Use_for, length_for_pass))

#Show the pass generated#
print("Your password is "+password)