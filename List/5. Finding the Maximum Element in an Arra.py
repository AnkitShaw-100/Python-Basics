# Finding the Maximum Element in an Array
n = int(input("Enter the length of array"))
a = [] 

# Accepting the values from user
for i in range (0,n):
    m = int(input("Enter the elements of the array : "))
    a.append(m)

# Finiding the maximum element in the array
m = max(a)
c = min(a)

# Printing the maximum && minimum 
for i in range (0,n):
      print(f"Entered array is:{a[i]}")

print(f"Maximum : {m}")
print(f"Minimum : {n}")