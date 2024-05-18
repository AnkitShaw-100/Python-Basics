n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))
n3 = int(input("Enter 3rd number"))

if n1>n2 and n1>n3 : 
 print("Maximum = ", n1)
elif n2>n1 and n2>n3 :
 print("Maximum = ", n2)
elif n3>n1 and n3>n2 :
 print("Maximum = ", n3)  
else :
 print("All are same")

if n1<n2 and n1<n3 : 
 print("Minimum = ", n1)
elif n2<n1 and n2<n3 :
 print("Minimum = ", n2)
elif n3<n1 and n3<n2 :
 print("Minimum = ", n3)  
else :
 print("All are same")
