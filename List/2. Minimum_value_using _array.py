# Find the Smallest Number:
n  =  int(input ("Enter the size of Array : "))
array1 = []

for i in range(n):
    element = int(input(f"Enter Elements {i+1} : "))
    array1.append(element)
print("The entered array is : " ,array1)
 
min_value = array1[0] 
for i in range(n):
    if array1[i] < min_value:
     min_value = array1[i] 

print("The largest number in the array ", min_value)