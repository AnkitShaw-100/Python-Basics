#Mean_&_Standard Deviation
import math 
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 3rd number: "))
n5 = int(input("Enter 3rd number: "))

l1 = [n1, n2, n3, n4, n5]

mean = (n1 + n2 + n3 + n4 + n5)/5
print("The mean of the 5 inputs are " ,mean)
i=0 
sum=0
n=0
while i<5 :
 n = (l1[i] - mean)**2
 sum += n
 i += 1    
sigma =  math.sqrt(sum/5)
print("The Standard deviation of the 5 inputs are " ,sigma)
