#WAP in Python  to to replace a word a per user
n = input("Enter a String : ")
check = input("Enter the word to be replaced in the String : ")
replace  = input("Enter the new word for the String : ")
l = len(n)
for i in range(0,l,1):
    if check == n[i]:
        new = n.replace(n[i],replace)
        print(f"The new string is {new}")
        
    else:
     print("Similar word is not found")
