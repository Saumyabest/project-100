a = [["abc0001","Bobby",100],
     ["abc0002","Larry",400],
     ["abc0003","Dan",150],
     ["abc0004","Billy",200],
     ["abc0005","Sid",350]]
     

def balance(v):
    for b in a:
        if (b[0] == v):
            name=b[1]
            bal=b[2]
            print("Hello "+name)
            print("Your balance is: "+ str(bal))
        else:
            print("This ID is not registered with the bank.")


def deposit(v):
    dep = int (input("Enter amount you want to deposit: "))
    for c in a:
        if(c[0] == v):
            bal=c[2]
            bal = bal + dep
            print("Your current balance is: "+ str(bal))
        else:
            print("This ID is not registered with the bank.")

def drawCash(v):
    draw = int (input("Enter amount you want to draw: "))
    for d in a:
        if(d[0] == v):
            bal=d[2]
            bal = bal - draw
            print("You Current balance is: "+ str(bal))
        else:
            print("This ID is not registered with the bank.")

def main():
    ID = input("Enter your ID ")
    print("Cash Withdrawl - Press 1 ")
    print("Cash Deposit - Press 2")
    print("Check Balance - Press 3")
    Enter = int(input("Enter your input: "))
    if(Enter == 1):
        drawCash(ID)
    elif(Enter == 2):
        deposit(ID)
    elif(Enter == 3):
        balance(ID)
    else:
        print("Enter the correct option")

main()