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

    # Show Details
    def showDetails(self):
        accNumber = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))
        userData = [
            i for i in Bank.data if i["accountNo."] == accNumber and i["pin"] == pin
        ]
        if not userData:
            print("Sorry! No account found of this account number")
        else:
            print("\nYour account information are:")
            for i in userData[0]:
                print(f"{i}: {userData[0][i]}")

    # Update Details
    def updateDetails(self):
        accNumber = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNumber and i["pin"] == pin
        ]

        if not userData:
            print("Sorry! No account found of this account number")
        else:
            print("You cannot change the age, account number, balance")
            print("Fill the details to change or leave it empty if no change")

        newData = {
            "name": input("Please enter new name or press enterto skip: "),
            "email": input("Please enter your new email or press enter to skip: "),
            "pin": input("Please enter your new pin or press enter to skip: "),
        }

        if newData["name"] == "":
            newData["name"] = userData[0]["name"]

        if newData["email"] == "":
            newData["email"] = userData[0]["email"]

        if newData["pin"] == "":
            newData["pin"] = userData[0]["pin"]

        newData["age"] = userData[0]["age"]
        newData["accountNo."] = userData[0]["accountNo."]
        newData["balance"] = userData[0]["balance"]

        if type(newData["pin"]) == str:
            newData["pin"] = int(newData["pin"])

        for i in newData:
            if newData[i] == userData[0][i]:
                continue
            else:
                userData[0][i] = newData[i]

        Bank.__update()
        print("Details updated successfully!")

    # Delete User Details
    def deleteUserDetails(self):
        accNumber = input("Please enter your account number: ")
        pin = int(input("Please enter your pin: "))

        userData = [
            i for i in Bank.data if i["accountNo."] == accNumber and i["pin"] == pin
        ]

        if not userData:
            print("Sorry! No account found with this account number")
            return

        check = input(
            "Press y if you want to delete your account or press n for not deleting the account: "
        )

        if check.lower() == "n":
            print("Account not deleted!")

        elif check.lower() == "y":
            Bank.data.remove(userData[0])
            Bank.__update()
            print("Account deleted successfully!")

        else:
            print("Invalid input! Please enter y or n.")


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

if check == 4:
    user.showDetails()

if check == 5:
    user.updateDetails()

if check == 6:
    user.deleteUserDetails()
