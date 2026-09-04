import random
import json
import string
from pathlib import Path


class Bank:
    database = Path("data.json")
    data = []

    # ------------------------------------
    # Load database
    # ------------------------------------
    @classmethod
    def load_data(cls):
        try:
            if cls.database.exists():
                with open(cls.database, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                    if content:
                        cls.data = json.loads(content)
                    else:
                        cls.data = []
            else:
                cls.data = []
                cls.update_database()

        except (json.JSONDecodeError, OSError):
            cls.data = []

    # ------------------------------------
    # Save database
    # ------------------------------------
    @classmethod
    def update_database(cls):
        try:
            with open(cls.database, "w", encoding="utf-8") as file:
                json.dump(cls.data, file, indent=4)

            return True

        except OSError:
            return False

    # ------------------------------------
    # Generate unique account number
    # ------------------------------------
    @classmethod
    def generate_account_number(cls):

        while True:
            letters = random.choices(string.ascii_uppercase, k=4)
            numbers = random.choices(string.digits, k=6)

            account_number = "".join(letters + numbers)

            random_list = list(account_number)
            random.shuffle(random_list)

            account_number = "".join(random_list)

            existing_account = any(
                user["accountNo"] == account_number for user in cls.data
            )

            if not existing_account:
                return account_number

    # ------------------------------------
    # Find user
    # ------------------------------------
    @classmethod
    def find_user(cls, account_number, pin):

        for user in cls.data:

            if user["accountNo"] == account_number and str(user["pin"]) == str(pin):
                return user

        return None

    # ------------------------------------
    # Create account
    # ------------------------------------
    @classmethod
    def create_account(cls, name, age, email, pin):

        name = name.strip()
        email = email.strip()

        if not name:
            return False, "Name cannot be empty.", None

        if age < 18:
            return False, "You must be at least 18 years old.", None

        if "@" not in email or "." not in email:
            return False, "Please enter a valid email address.", None

        if not str(pin).isdigit() or len(str(pin)) != 4:
            return False, "PIN must contain exactly 4 digits.", None

        account_number = cls.generate_account_number()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "accountNo": account_number,
            "balance": 0,
        }

        cls.data.append(user)

        if cls.update_database():

            return (
                True,
                "Account created successfully.",
                account_number,
            )

        cls.data.remove(user)

        return False, "Unable to save account.", None

    # ------------------------------------
    # Deposit money
    # ------------------------------------
    @classmethod
    def deposit(cls, account_number, pin, amount):

        user = cls.find_user(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Deposit amount must be greater than 0."

        if amount > 100000:
            return False, "Maximum deposit allowed is Rs. 100,000."

        user["balance"] += amount

        cls.update_database()

        return (True, f"Rs. {amount:,} deposited successfully.")

    # ------------------------------------
    # Withdraw money
    # ------------------------------------
    @classmethod
    def withdraw(cls, account_number, pin, amount):

        user = cls.find_user(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Withdrawal amount must be greater than 0."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount

        cls.update_database()

        return (True, f"Rs. {amount:,} withdrawn successfully.")

    # ------------------------------------
    # Get account details
    # ------------------------------------
    @classmethod
    def get_details(cls, account_number, pin):

        user = cls.find_user(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN.", None

        return True, "Account found.", user

    # ------------------------------------
    # Update account
    # ------------------------------------
    @classmethod
    def update_account(
        cls,
        account_number,
        pin,
        name=None,
        email=None,
        new_pin=None,
    ):

        user = cls.find_user(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        if name:
            user["name"] = name.strip()

        if email:

            if "@" not in email or "." not in email:
                return False, "Please enter a valid email."

            user["email"] = email.strip()

        if new_pin:

            if not str(new_pin).isdigit() or len(str(new_pin)) != 4:
                return False, "PIN must contain exactly 4 digits."

            user["pin"] = int(new_pin)

        cls.update_database()

        return True, "Account information updated successfully."

    # ------------------------------------
    # Delete account
    # ------------------------------------
    @classmethod
    def delete_account(cls, account_number, pin):

        user = cls.find_user(account_number, pin)

        if not user:
            return False, "Invalid account number or PIN."

        cls.data.remove(user)

        cls.update_database()

        return True, "Account deleted successfully."


# Load database when program starts
Bank.load_data()