#Counting Even and Odd
n = int(input("Enter the length of array : "))
a = []
e = 0
o = 0

#Accepting value in an array 
for i in range(0,n):
    m =  int(input("Enter only integer values : "))
    a.append(m)

#Counting even_odd
for i in range(0,n):
    if a[i] == 0:
        print(f"{a[i]} is '0' ")
    elif a[i] % 2 == 0:
        e += 1
        print(f"{a[i]} is a Even number") 
    else :
        o += 1
        print(f"{a[i]} is a Odd number")
    
print(f"Total count of even number is {e} and odd number is {o}")