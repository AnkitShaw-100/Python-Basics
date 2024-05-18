# Armstrong number
n = int(input("Enter a number: "))
s = 0  
c = 0
m = n

temp = n
while temp > 0:
    temp = temp // 10
    c += 1
temp = n  

while temp > 0:
    r = temp % 10
    s += pow(r, c)
    temp = temp // 10

if m == s:
    print(f"Given number {m} is an Armstrong Number")
else:
    print(f"Given number {m} is NOT an Armstrong Number")
