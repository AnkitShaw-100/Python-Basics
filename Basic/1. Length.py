# Count Characters in a String:
n = (input("Enter a String : "))  
count = 0
for char in n:
    count += 1
print(f"The given String has {count} letters")

#OR

n = (input("Enter a String : "))  
l = len(n)
print(f"The given String has {l} letters")
