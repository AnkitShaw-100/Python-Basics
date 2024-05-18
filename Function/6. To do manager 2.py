#To do manager 2

# LOGIC
#To accept the Tasks one by one 
#Accept more Tasks from the user 
#To print the Tasks Enetred by the user
#-------------------------------------------------------------------------------------------------------------------
m = [] 
n = input("Enter Your first task : ")
m = m.append(n)
d = 0

# Taking more task from the user
def main(): 
    c = int(input("Press 5 to enter more task :"))
    if c == 5 :
        m = m.extend(1)
    task = input("Enter your task")
    m.insert(1, "task")


#Adding more tasks    
def repeat():
     k = int(input("Enter 7 to Enter new task"))
     if k == 7:
        d += 1 
        main()
     L = int(input("Enter 9 to Stop adding task"))
     if k == 9: 
       output()

#Printing the tasks 
def output():
    for i in range(0,d+2):
        print(f"Your Task for the day are : {m[i]}")

    
if __name__ == "__main__":
    main()