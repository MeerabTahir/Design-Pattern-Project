import sys
from getpass import getpass

class ATM:
    def __init__(self, name, acc_no, bal=0):
        self.name = name
        self.acc_no = acc_no
        self.bal = bal  # balance

print("*******WELCOME TO BANK OF PAKISTAN*******")
print("--------------------------------------------------\n")

pin_a = getpass("Enter your 4-digit Pin: ")
pin_b = getpass("Re-enter your 4-digit Pin: ")

if pin_a == pin_b:
    print("------ACCOUNT DETAILS------")
    name = input("What's your name? ")
    acc = input("Account number: ")
    print("Great! Account ready...\n")

    client = ATM(name, acc)

    flag = True
    while flag:
        tr = input("Do anything? (y/n): ")
        if tr == "y":
            print("1. See Balance\n2. Put Money\n3. Take Money\n4. Send\n5. Leave")

            try:
                pick = input("Pick 1-5: ")
                op = int(pick)
            except:
                print("No letters allowed!\n")
                continue

            if op == 1:
                print("----INFO----")
                print("Name:", client.name.upper())
                print("Number:", client.acc_no)
                print("Balance: Rs", client.bal)

            elif op == 2:
                add = input("How much to deposit? ")
                client.bal = client.bal + int(add)
                print("Now you have Rs", client.bal)

            elif op == 3:
                cut = input("Withdraw amount: ")
                cut = int(cut)
                if cut > client.bal:
                    print("Low funds. Balance: Rs", client.bal)
                else:
                    client.bal = client.bal - cut
                    print("Done. Remaining: Rs", client.bal)

            elif op == 4:
                send = int(input("How much to send? "))
                if send > client.bal:
                    print("Not enough balance. Rs", client.bal)
                else:
                    client.bal -= send
                    print("Sent Rs", send)
                    print("Now: Rs", client.bal)

            elif op == 5:
                print("Thanks for using BOP. Bye!")
                flag = False
            else:
                print("Invalid! Only 1 to 5\n")
        elif tr == "n":
            print("See you later. Thanks!")
            flag = False
        else:
            print("Wrong input. Use y/n only.\n")
else:
    print("Pins don’t match. Try again.")
