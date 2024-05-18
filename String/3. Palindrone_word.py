#Palindrone_word
n = input("Enter a string : ")

x = (n[::-1])

if x == n:
    print(f"Given word is a Palindrone Word : {x}")
else :
    print(f"Given word is not a Palindrone word : {x}")