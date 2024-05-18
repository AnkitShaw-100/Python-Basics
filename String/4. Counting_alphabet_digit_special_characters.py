#Counting_alphabet_digit_special_character
n = input("Enter a String : ")
l = len(n)
a = 0 
num = 0 
sp = 0
for i in range (0,l):
    if n[i].isalpha(): 
        a = a + 1
    elif n[i].isnumeric():
        num = num + 1
    else :
        sp += 1 
print(f"Entered String has {a} Alphabets ") 
print(f"Entered String has {num} Numeric_values ")
print(f"Entered String has {sp} Special_Characters ")