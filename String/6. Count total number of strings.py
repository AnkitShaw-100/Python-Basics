#Count total number of strings
n = input("Enter a string : ")
c = 0
l = len(n)
for i in range (0,l,1):
    c += 1
    print (f"The letters are = {n[i]}")
print (f"Total number of letters found is = {c}")
    