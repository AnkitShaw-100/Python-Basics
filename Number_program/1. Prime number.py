# Prime_number
n = int(input("Enter a number to check whether it is prime or not : "))
c = 0
for i in range (1, n+1):
    if n % i == 0 :
        c += 1  
if c == 2 : 
    print (f"Entered number is a Prime number : {n} ") 
else : 
    print (f"Not a Prime number : {n} ") 