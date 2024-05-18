#Count the frequency of given character
n = input("Enter a String : ")
m = len(n)
c=0
letter = input("Enter a letter to be searched in the string : ")
for i in range(0,m,1):
    if (n[i]==letter):
        c += 1
        print(f"Letter found at position : {i}")
print(f"Letter found {c} times")