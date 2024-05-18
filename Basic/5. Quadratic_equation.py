#Quadratic_Eqn
import math
a = int(input("Enter the value of a for calculation of roots")) 
b = int(input("Enter the value of b for calculation of roots"))
c = int(input("Enter the value of c for calculation of roots"))
discriminant = b**2 - 4*a*c
F1 = (-b + (math.sqrt(discriminant)))/(2*a)
F2 = (-b - (math.sqrt(discriminant)))/(2*a)

print("The roots are = ",F1,F2)
