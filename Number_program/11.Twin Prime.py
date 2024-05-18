#Twin Prime 
n =  int(input("Enter a number : "))
n1 = n 
m =  int(input("Enter another number : "))
m1 = m 
c = 0 
for  i in range (1, n+1):
    if n % i == 0 :
        c += 1 
if c == 2 :
    print("Given number is prime")
    print("------Checking 2nd number------")
else :
    print("Given number is not a prime number ")

d = 0
for  i in range (1, n+1):
    if n % i == 0 :
         d += 1 
if d == 2 :
    print("Given number is also prime")
    print("------Checking whether it is a Twin prime number------")
else :
    print("Given number is not a prime number ")

if abs(n1-m1) == 2 :
    print(f"Given numbers are a Twin prime {n},{m}.")  
else :
    print(f"Given numbers are NOT a Twin prime {n},{m}.")
    
    

