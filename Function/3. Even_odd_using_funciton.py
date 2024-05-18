#even_odd_using_funciton
def even_odd(n):
    
    if n == 0:
        print(f"{n} is an Invalid input : ")
    elif n % 2 == 0:
        print(f"{n} is a Even number") 
    elif n % 3 == 0:
        print(f"{n} is a Odd number")
    else :
        print(f"{n} Prime number")

def main():
    m = int(input("Enter a number : "))
    z = even_odd(m)
    print("Program compiled successfully!!")
        
if __name__=="__main__":
    main()