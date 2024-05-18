# Sorting a list
n = int(input("Enter the length of array: "))
a = []

# Accepting values in an array
for i in range(n):
    m = int(input("Enter only integer values: "))
    a.append(m)

#Ascending order
a.sort()
print(f"Sorted array in ascendding order : {a}")

#Decending order
a.sort(reverse=True)
print(f"Sorted array in descending order : {a}")
