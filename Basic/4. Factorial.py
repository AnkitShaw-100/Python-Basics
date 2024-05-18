#Write a Python program to calculate the factorial of a given positive integer. The program should take an integer as input and compute its factorial.
#Here are the steps to accomplish this:
# 1.Prompt the user to enter a positive integer.
# 2.Check if the input is valid (positive integer). If not, display an error message and ask for input again.   
# 3.Calculate the factorial of the input integer.
# 4.Display the result.
 
import sys
n = int(input("Enter a positive number :"))
if(n > 0):
 print("The number is postive")
if(n < 0):
 print("The number is negative")
 sys.exit()

m = 1
for i in range(1,n+1):
 m = m * i

print("The factorial of a given number : ",m)