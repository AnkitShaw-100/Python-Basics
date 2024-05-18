# Pizza_Delivery
address = input("Enter your address: ")
small = 5
medium = 7
large = 10

size = input("S = Small size, M = Medium size, L = Large size: ")

if size == "S":
    n = int(input("If you want Extra cheese, press 1. Or press any other number to skip: "))
    if n == 1:
        print("You will be charged $2 extra for it")
        small = small + 2
    else:
        small = small + 0

    n = int(input("If you want Extra Toppings, press 2. Or press any other number to skip: "))
    if n == 2:
        print("You will be charged $1 extra for it")
        small = small + 1
    else:
        small = small + 0

    n = int(input("If you want Coke, press 3. Or press any other number to skip: "))
    if n == 3:
        print("You will be charged $2 extra for it")
        small = small + 2
    else:
        small = small + 0

    total_bill = small

elif size == "M":
    n = int(input("If you want Extra cheese, press 1. Or press any other number to skip: "))
    if n == 1:
        print("You will be charged $2 extra for it")
        medium = medium + 2
    else:
        medium = medium + 0

    n = int(input("If you want Extra Toppings, press 2. Or press any other number to skip: "))
    if n == 2:
        print("You will be charged $1 extra for it")
        medium = medium + 1
    else:
        medium = medium + 0

    n = int(input("If you want Coke, press 3. Or press any other number to skip: "))
    if n == 3:
        print("You will be charged $2 extra for it")
        medium = medium + 2
    else:
        medium = medium + 0

    total_bill = medium

elif size == "L":
    n = int(input("If you want Extra cheese, press 1. Or press any other number to skip: "))
    if n == 1:
        print("You will be charged $2 extra for it")
        large = large + 2
    else:
        large = large + 0

    n = int(input("If you want Extra Toppings, press 2. Or press any other number to skip: "))
    if n == 2:
        print("You will be charged $1 extra for it")
        large = large + 1
    else:
        large = large + 0

    n = int(input("If you want Coke, press 3. Or press any other number to skip: "))
    if n == 3:
        print("You will be charged $2 extra for it")
        large = large + 2
    else:
        large = large + 0

    total_bill = large

else:
    print("Invalid Input")
    total_bill = 0

if total_bill > 0:
    print(f"Your pizza will be delivered to address: {address}")
    print(f"Your bill: ${total_bill}")
    print("Thank You! Visit again!!")
