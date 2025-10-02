"""
PROGRAM NAME: BANKING SOFTWARE
AUTHOR: iMOLE K.
"""

mnm = 45

def readBankFile():
    bk = {}
    f = open("bank.txt")
    list_accounts = f.readlines()
    f.close()
    for profile in list_accounts:
        ls = profile.rstrip("\n").split(",")
        name = ls[0]
        amount = float(ls[1])
        bk.update({name:amount})
    
    return bk


def persistBank(data):
    """this update the bank.txt file"""
    content = ""
    
    for k,v in data.items():
        content += f"{k},{v}\n"
    
    f = open("bank.txt", "w")
    f.write(content)
    f.close()


BANK = readBankFile()

print("***Welcome to CASHIE BANK***")

services = """
**************************
What To do:              *
1. CREATE ACCOUNT        *
2. CHECK BALANCE         *
3. DEPOSIT               *
4. WITHDRAW              *
5. Convert to Naira      *
6. QUIT                  *
**************************
"""
while True:
    print(services)

    choice = input("SELECT (1 - 5): ")

    if choice == "1":
        print("To Create account please enter your name")
        name = input("Enter Name: ")
        initial_amount = float(input("Enter Your Initial Amount: "))
        BANK[name] = initial_amount
        persistBank(BANK)

        print(f"ACCOUNT CREATED SUCCESSFULLY!, account name is {name}")
    elif choice == "2":
        print("To Check Your Balance, please provide account name")
        account_name = input("Enter account Name: ")
        bal = BANK.get(account_name)
        if bal == None:
            print("Account does not exist, ole!")
        else:
            print(f"Welcome Back {account_name}")
            print(f"***Your balance is ${bal}***")
    
    elif choice == "3":
        print("To Deposit,please provide your account name")
        accnt = input("Enter Account Name: ")
        amount = float(input("Enter amount to deposit: "))
        try:
            BANK[accnt] += amount
            
            persistBank(BANK)
            print("Deposited successfully")
        except:
            print("Sorry, You have no account with us!")
    
    elif choice == "4":
        print("To Withdraw,please provide your account name")
        accnt = input("Enter Account Name: ")
        amount = float(input("Enter amount to Wthdraw: "))
        try:
            if BANK[accnt] >= amount:
                BANK[accnt] -= amount
                persistBank(BANK)
                print("Withdrawal successfull")
            else:
                print("OLE, account insufficient!")
        except:
            print("Sorry, You have no account with us!")
    elif choice == "5":
        print("To Convert your balance,please provide your account name")
        accnt = input("Enter Account Name: ")
        val = BANK.get(accnt)
        if val == None:
            print("Sorry, You have no account with us!")
        else:
            print(f"Your balance is converted and it os N{val*1500}")
        pass
    elif choice == "6":
        print("THAN YOU FOR USING OUR BANK")
        break
    else:
        print("invalid choice, please select between 1 - 5")


print("**************************")
