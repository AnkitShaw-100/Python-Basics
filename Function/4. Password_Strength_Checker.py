# Password Strength Checker

def checking(n):
   l = len(n)             
   print(l)
   dn = n.isalnum()
   print(dn)
   if l > 8 and dn == True :
        print("Your password is strong")
   elif l > 8 or dn == True :
        print( "Your password is not so strong" )
   elif l <= 8:
        print( "Your password is too weak" )
   else:
        print( "Enter a valid password" )


   m = int(input("To restart the program press 1 : "))
   if m == 1:
        main()
   else:
        print("Invalid Input")

def main():
    n = input ("Enter a string : ")
    checking(n)

if __name__ == "__main__":
    main()
    
