#Searching for an element in array
n = int(input("Enter the size of array : "))
a = []
 
#Accepting value in an array
for i in range(0,n):
    p = input("Enter the elements of array : ")
    a.append(p)

search = input("Enter the value to be searched : ")
#Searching for the given value 
for i in range(0,n):
    if a[i] == search:
       print(f"The given serach value is found at {i+1} position")
    else:
        exit

#Adding new element 
def adding():
    if k == 1:
        new_element = input("Enter a new element to be inserted in the array : ")    # Enter another element to replace it
    for i in range(0,n):
        if a[i] == search:
            a[i] = new_element
            print(f"New array is : {a}")
    else:
      exit

#Removing element
def reemoving():
    for i in range(0,n):
     if a[i] == search:
            a[i] = 0
            print(f"New array is : {a} ")


k = int(input("Press 1 to add new element, Press 2 to remove an element :  "))
if(k == 1):
    print(f"The givem list is : {a}")
    adding()
elif(k == 2):
    print(f"The givem list is : {a}")
    reemoving()
else:
    exit
     

