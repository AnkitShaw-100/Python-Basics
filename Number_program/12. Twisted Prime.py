# Twisted Prime 
n = int(input("Enter a number : "))
c = 0
z = 0 


#Checking the given number is prime or not 
for  i in range (1, n+1):
    if n % i == 0 :
        c += 1 
if c == 2 :
    print("Given number is prime")
    z += 100
else :
    print("Given number is not a prime number ")


#Counting the length of number
temp = n 
l = 0 
while temp > 0: 
    temp = temp // 10
    l += 1 



#Reversing the number 
# l -= 1
s = 0
temp = n 
while temp > 0:
    r = temp % 10
    l -= 1
    s = s +(10**l * r)
    temp = temp // 10 
print(s)

#Again checking for prime 
m = 0  
for  i in range (1, s+1):
    if s % i == 0 :
        m += 1 


#Checking are both number prime 
if m == 2:
    print("Given number is prime")
    z += 100
else:
    print("Given number is not a prime number ")

if z == 200:
    print("Given number is a twisted prime number ")
else:
    print("Given number is NOT a twisted prime number ")
