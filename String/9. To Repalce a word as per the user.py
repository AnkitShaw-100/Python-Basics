# To extarcat a word as per the user 
n = input("Enter a String : ")
check = input("Enter the word to be replaced in the String : ")
replace  = input("Enter the new word for the String : ")
l = len(n)
c = 0 
for i in range(0,l,1):
    if n[i] == ' ':
        x = n.split(' ')
print(f"Entered String{x}")

m = len(x)
for i in range(0,m,1):
    if x[i] == check:
        x[i] = replace
print(f"New String is Entered String is {x}")           
