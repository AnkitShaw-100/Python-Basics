# WAP in Python to separate individual character from string
#Reverse Order
n = input("Enter a string : ")
l = len(n)
m = l-1
for i in range (m,-1,-1):
    print(n[i])
print()
print()

#Normal Order
for i in range(0,l,1):
    print(n[i])