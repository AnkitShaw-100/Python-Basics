#password strength checker
n = input("Enter your password")
l = len(n)
dn = n.isalnum()
print(l)
print(dn)
if( l > 8 ) and ( dn == True ):
    print("Your password is strong")
elif( l > 8 ) or ( dn == True ):
    print( "Your password is not so strong" )
elif( l <= 8 ) :
    print( "Your password is too weak" )
else:
    print( "Enter a valid password" )