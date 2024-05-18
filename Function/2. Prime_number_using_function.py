#prime_number
def _prime_(n):
    c = 0   
    for i in range (1, n+1):
        if n % i == 0 :
            c += 1  
    if c == 2 : 
        return True 
    else :
        return False 
     
     #issue
     #issue
     #issue
     #issue
     #issue
     #issue
def  main():

    m =  int(input("Enter a number : "))
    z = _prime_(m)
    print(z)
    if _prime_(z):
        print(f"{m}is a prime number")
    else :
        print(f"{m} is NOT a prime number")

if __name__=="__main__":
    main()

