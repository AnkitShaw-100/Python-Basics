#Maximimum_Minimum
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))

if n1 == n2 == n3:
    print("All are same")
else:
    l1 = [n1, n2, n3]
    l1.sort()

    print("The minimum value inserted = ", l1[0])  # Access the first (smallest) element in the sorted list
    print("The maximum value inserted = ", l1[2])  # Access the last (largest) element in the sorted list
