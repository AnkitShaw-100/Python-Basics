# Roller_coaster
age = int(input("Enter your age: "))

if age < 0:
    print("Invalid Input")
elif age >= 18:
    print("You are eligible for the Ride!!")
else:
    print("You are not eligible for the Ride!!")

height = int(input("Enter your height in cm: "))

if height >= 150:
    print("You are eligible for the Ride!!")
else:
    print("You are not eligible for the Ride!!")

amount = 5
n = int(input("If you want a pic of your ride, press 1: "))

if n == 1:
    print("It will charge you an extra $1 !!")
    amount += 1

print(f"Your total bill is ${amount}")
print("Thank You!!")
