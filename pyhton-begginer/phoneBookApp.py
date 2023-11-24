import csv

def save_csv(accounts):
    try:
        with open('accounts.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["account number", "owner", "Balance"])
            for account_number, account_info in accounts.items():
                writer.writerow([account_number, account_info['owner'], account_info['balance']]) 
    except FileNotFoundError:
        print("No existing account data found.")

def load_csv(accounts):
    try:
        with open('accounts.csv', newline='') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                account_number, owner, balance = row
                accounts[int(account_number)] = {"owner": owner, "balance": float(balance)}
    except FileNotFoundError:
        print("No existing account data found.")

def create_account(accounts, owner, balance=0):
    account_number = len(accounts) + 1
    accounts[account_number] = {"owner": owner, "balance": balance}
    return account_number

def deposit(accounts, account_number, amount):
    accounts[account_number]['balance'] += amount
    return accounts[account_number]['balance']

def withdraw(accounts, account_number, amount):
    if amount > accounts[account_number]['balance']:
        print("Insufficient funds!")
        return
    accounts[account_number]['balance'] -= amount
    return accounts[account_number]['balance']

def get_balance(accounts, account_number):
    return accounts[account_number]['balance']

def main():
    accounts = {}
    load_csv(accounts)

    while True:
        print("\nBank Account Management System")
        print("1. Create a new account")
        print("2. Login to an existing account")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            name = input("Enter your name: ")
            deposit_amount = float(input("Enter initial deposit: "))
            account_number = create_account(accounts, name, deposit_amount)
            save_csv(accounts)
            print(f"Account created successfully! Your account number is {account_number}")

        elif choice == "2":
            acc_num = int(input("Enter your account number: "))

            if acc_num not in accounts:
                print("Account not found!")
                continue

            while True:
                print(f"\nWelcome {accounts[acc_num]['owner']}!")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Logout")

                choice = input("Choose an option (1/2/3/4): ")

                if choice == "1":
                    print(f"Your balance is: ${get_balance(accounts, acc_num)}")
                elif choice == "2":
                    amount = float(input("Enter amount to deposit: "))
                    deposit(accounts, acc_num, amount)
                    save_csv(accounts)
                    print(f"Deposited successfully! New balance: ${get_balance(accounts, acc_num)}")
                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: "))
                    withdraw(accounts, acc_num, amount)
                    save_csv(accounts)
                    print(f"Withdrawal successful! New balance: ${get_balance(accounts, acc_num)}")
                elif choice == "4":
                    break
                else:
                    print("Invalid choice! Please choose again.")

        elif choice == "3":
            save_csv(accounts)
            print("Thank you for using the Bank Account Management System!")
            break

        else:
            print("Invalid choice! Please choose again.")

if __name__ == "__main__":
    main()
