# Niven number
# Sum of the digits of the number = 1 + 4 = 5. So, 14 is not divisible by 5.
# Hence, 14 is not a Niven number.
# Some other examples of Niven numbers include 1, 2, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20 etc.
n = int(input("Enter a number to check whether it is a Niven number or not : "))
m = n 
s = 0
while n>0 :
    r = n % 10
    s = s + r
    n = n // 10
if m % s == 0 : 
    print("Given number is a Niven number ")
else : 
    print("Given number is NOT a Niven number ") 