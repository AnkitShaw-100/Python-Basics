#spy_number_using_function
def spy(n):
    s = 0
    m = 1
    while n > 0 :
        r = n % 10
        s += r
        m *= r 
        n = n//10
    if s == m :
        return True
    else :
        return False
    
def main():
    a = int(input("Enter a number : "))
    z = spy(a)
    if spy(z):
        print(f"{a} the given number is a spy number")
    else:
        print(f"{a} the given number is NOT a spy number")


if __name__ == "__main__":
    main()     