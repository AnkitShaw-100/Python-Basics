# Pronic number 
n = int(input("Enter a number to check whether it is a Pronic number or not: "))
m1 = n
m = int(n / 2)
c = 0

for i in range(0, m):
    r = i * (i + 1)
    if r == m1:
        c += 1
         
if  c == 1 :
    print("Given number is a Pronic number")
else:
    print("Given number is NOT a Pronic number")
