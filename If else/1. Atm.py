# 1.Write a Python program that simulates a simple ATM.
# 2.The program should allow the user to check their account balance, deposit money, and withdraw money. 
# 3.You should also include error handling for cases like insufficient balance or invalid inputs.
import random
import sys
atm_pin=1000
n = int(input("Press 1 to check account balance\nPress 2 if you want to deposit money or withdraw money "))

if(n == 1):
 account_number = input("Enter you 10- digit account number")
 l = len(account_number)
 if(l == 10):
    print ("Account number accepeted")
 else:
    print("Invalid account number") 
    sys.exit()
 input_atm_pin = int(input("Enter your pin to check account balance"))
 if(input_atm_pin == atm_pin):
  print("Login Successful")
  random_1 = random.randint(100,100000)
  print("Your account balance is :$",(random_1))
 else:
  print("Wrong atm pin")
 
if (n == 2):
 account_number = input("Enter you 10- digit account number")
 l = len(account_number)
 if(l == 10):
    print ("Account number accepeted")
 else:
    print("Invalid account number") 
    sys.exit()
 a =  int(input("Press 1 to Deposit money\nPress 2 to withdraw money"))
 if(a == 1):
  input_amount_1 = int(input("Enter your amount you want to deposit"))
  random_2 = random.randint(100,100000)
  print("Your account balance is :$",(random_2))
  new_account_balance_1= random_2 + input_amount_1
  print("Your account is credited with :$",input_amount_1)
  print("Your new account balance is :$",new_account_balance_1)
 if(a == 2):
  input_amount_2 = int(input("Enter your amount you want to withdraw"))
  random_3 = random.randint(100,100000)
  print("Your account balance is :$",(random_3)) 
  new_account_balance_2 =  random_3 - input_amount_2 
  if(new_account_balance_2 < 0):
   print("Insufficient balance")
  else:
   print("Your new account balance is :$",new_account_balance_2)
  
print("Thank You for using SBI ATM !!")

   

