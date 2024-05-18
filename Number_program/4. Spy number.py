# Spy number

n = int(input("Enter a number to check whether it is a Pronic number or not: "))
m = n 
p = 1
s = 0
while n > 0 :
    r = n % 10
    s = s + r
    p = p * r
    n = n // 10
if s == p:
 print("The given number is a Spy number ")
else : 
 print("The given number is NOT a Spy number ")