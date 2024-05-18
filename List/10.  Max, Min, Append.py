# Max, min, append, sort, reverse
b = [10, 20, 30, 40, 60]

print(b)

# 1. Printing the max value
c = max(b)
print("The max value of the array is:", c)

# 2. Printing the min value
d = min(b)
print("The min value of the array is:", d)

# 3. Adding an element to the list
print("Before adding an element to the list:", b)
b.append("META")
print("After adding an element to the list:", b)

# 4. Sort
print("Before sorting:", b)
b.sort()
print("After sorting:", b)

# 5. Reverse
print("Before reversing:", b)
b.reverse()
print("After reversing:", b)
