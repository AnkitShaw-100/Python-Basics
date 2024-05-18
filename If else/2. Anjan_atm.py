import random


def valid_acc(balance) :

    n = 0

    while n <= 3 :
        acc_pin = int(input("Enter your 4 digit pin : "))
        l = len(str(acc_pin))
        if l == 4 :
            check = int(input("1 -> check balance \n2 -> withdraw"))
            if check == 1 :
                print(balance)
                break
            elif check == 2 :
                withdraw_money = int(input("Enter your amount"))
                if withdraw_money > balance :
                    print("Insuffiecient balance")
                    break
                elif withdraw_money < balance :
                    print("Here is your money : " , withdraw_money)
                    print("And your balance is : " , balance-withdraw_money)
                    break
        else :
            print("Wrong pin format")
            n +=1


balance = random.randint(0,100000)
n = 0
while n <= 3 :
    acc_num = int(input("Enter your 10 digit account number : "))
    l = len(str(acc_num))
    if l == 6 :
        valid_acc(balance)
        break
    else :
        print("Enter a valid account number")
    n+=1