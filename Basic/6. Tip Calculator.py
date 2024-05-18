#Tip Calculator
p = float(input("Enter the total amount of bill :$ "))
n = int(input("Enter the number of people splitting the bill : "))
percentage = int(input("Enter the % you wish to tip of the total amount : "))
total_amt = p +((percentage/100)*p)
bill_on_cash = total_amt/n
print(f"{n} each of you have to pay ${bill_on_cash} amount")
print("Thank you !!")
