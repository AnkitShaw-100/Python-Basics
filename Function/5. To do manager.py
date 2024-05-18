#To do manager

# LOGIC
#To accept the Tasks
#Accept more Tasks from the user 
#To print the Tasks Enetred by the user
#--------------------------------------------------------------------------------------------

def add_more(n):
    # Create an array with user-specified length
    m = [0] * n
    for i in range(0,n):
        m[i] = (input("Enter your tasks : "))

    #Printing the Task Entered
    for i in range(0,n):
        print(f"{i+1}.Your task for the day are : {m[i]}")

    #Restarting the program
    c = int(input("To restart the program press 1 : "))
    if c == 1:
        main()
    else:
        print("Invalid Input")


def main():
    n = int(input("Enter the number of task for the day : "))
    add_more(n)
    
if __name__ == "__main__":
    main()
    