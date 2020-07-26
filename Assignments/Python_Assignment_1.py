#Write a program which will find all such numbers which are divisible by 7 but are not a #multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be #printed in a comma-separated sequence on a single line.

nums=[]
for num in range(2000, 3201):
    if (num%7==0) and (num%5!=0):
        nums.append(str(num))
print("Total numbers are: ", len(nums))
print (", ".join(nums))

#Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.


first_name = input("Enter your First Name:").strip()
last_name = input("Enter your Last Name:").strip()
print("Your reversed name is: ", first_name[::-1]+" "+last_name[::-1])

#Write a Python program to find the volume of a sphere with diameter 12 cm.Formula: V=4/3 * π * r 3

import math

d = 12
r = d / 2
volume = 4/3 * math.pi * r**3
print("The Volume is:", volume)