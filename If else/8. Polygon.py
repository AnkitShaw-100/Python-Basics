#Polygon
n = input("Enter Triangle,Rectangle,Circle")
if n =="Triangle" :
 
 h = int(input("Enter the Height"))
 b = int(input("Enter the Base"))
 area1 = (h*b)/2
 s3 = int(input("Enter the 3rd side"))
 perimeter1 = h + b + s3
 print(area1)
 print(perimeter1)

elif n =="Rectangle" :
 
  l = int(input("Enter the Length"))
  b = int(input("Enter the Breadth"))
  area2 = (l*b)
  perimeter2 = 2*(l+b)
  print(area2)
  print(perimeter2)

elif n =="Circle" :
 
 r = int(input("Enter the Radius"))
 area3 = 3.14*r*r
 perimeter3 = 2*3.14*r
 print(area3)
 print(perimeter3)  
 
else :
 print("Invalid Input")