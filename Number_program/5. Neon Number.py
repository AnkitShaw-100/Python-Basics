# Neon number 

n = int(input("Enter a number to check whether it is a Neon number or not: "))
# m = n
sum=0
s=n*n
while s > 0:
    r = s % 10
    sum = sum + r
    s = s // 10
  
 

if sum == n:
    print("Given number is a Neon number")
else:
    print("Given number is NOT a Neon number") 
  