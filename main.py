import random
import json
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists!")
    except Exception as err:
        print(f"An error occures as {err}")

    # Update data in data.json file
    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            fs.write(json.dumps(Bank.data))

    # Generate Account Number
    @classmethod
    def __generateAccountNumber(cls):
        alpha = random.choices(string.ascii_letters, k=4)
        nums = random.choices(string.digits, k=4)
        spchar = random.choices("!@#$%^&*()", k=2)
        id = alpha + nums + spchar
        random.shuffle(id)
        return "".join(id)

    # Create Account
    def createAccount(self):
        info = {
            "name": input("Enter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your pin: ")),
            "accountNo.": Bank.__generateAccountNumber(),
            "balance": 0,
        }
        if info["age"] < 18:
            print("Sorry! you cannot create your account")
        elif len(str(info["pin"])) != 4:
            print("Please provide 4 digits pin")
        else:
            print("Your account has been created successfully!")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down your account number")

            Bank.data.append(info)
            Bank.__update()

    # Deposit Money
    def depositMoney(self):
        accNumber = input("Please tell your account number: ")
        pin = int(input("Please tell your pin: "))
        userData = [
            i for i in Bank.data if i["accountNo."] == accNumber and i["pin"] == pin
        ]
        if not userData:
            print("Sorry! No account found of this account number")
        else:
            amount = int(input("Enter amount you want to deposit: "))
            if amount > 100000:
                print("Sorry the amount is too much you can deposit below 1 lakh")
            elif amount < 0:
                print("Enter valid amount")
            else:
                userData[0]["balance"] += amount
                Bank.__update()
                print("Amount deposited successfully!")

    # Withdraw Money
    def withdrawMoney(self):
        accNumber = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))
        userData = [
            i for i in Bank.data if i["accountNo."] == accNumber and i["pin"] == pin
        ]

        if not userData:
            print("Sorry! No account found of this account number")
        else:
            amount = int(input("Enter amount you want to withdraw: "))
            if amount < amount:
                print("Sorry! you dont have that much money")
            elif amount < 0:
                print("Enter valid amount")
            else:
                userData[0]["balance"] -= amount
                Bank.__update()
                print("Amount withdrawed successfully!")


user = Bank()

print("Press 1 for crete an account: ")
print("Press 2 for depositing the money in the bank: ")
print("Press 3 for withdrawing the money from the bank ")
print("Press 4 for details of your bank account: ")
print("Press 5 for updating the details of your account: ")
print("Press 6 for deleting your account: ")

check = int(input("Please enter your response: "))

if check == 1:
    user.createAccount()

if check == 2:
    user.depositMoney()

if check == 3:
    user.withdrawMoney()
