# Sum of elements in an list
n = int(input("Enter the size of array : "))
a = []
sum = 0

# Accepting integers
for i in range(0,n):
    m = int(input("Enter the elements of the array : "))
    a.append(m)
    
# Sum of the elemets
for i in range(0,n):
    sum = sum + a[i] 

#Printing 
print(sum)