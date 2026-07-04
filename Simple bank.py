# - ✅ User authentication system
# - ✅ ATM operations
# - ✅ Menu-based navigation
# - ✅ Exit option
# - Login system with limited attempts
# - ATM functionalities (balance, deposit, withdraw)


is_true = True
attempts = 3
correct_password = 1410
balance = 10000

while is_true:
    print("--------------------------------")
    print("Banking console welcomes you!!!")
    print("--------------------------------\n")
    name = input("Enter your (Id/name): ")
    print(f"\nWelcome {name}!!!")

    is_login = input("Do you want to login (y/n): ")

    if is_login.lower() == "y":
        while attempts > 0:
            password = int(input("Enter your 4-digit password: "))

            if password == correct_password:
                print("---------------------------------------------------")
                print(f"Logged into {name}'s account successfully!")
                print("---------------------------------------------------")


                while True:
                    print("\n1.Balance\n2.Deposit\n3.Withdraw\n4.Exit")
                    choice = input("What do you want to do? : ")
                    print("---------------------------------------------------")

                    if choice == "1":
                        print(f"Current balance: ₹{balance}")
                    elif choice == "2":
                        deposit = float(input("Enter amount to deposit: "))
                        balance += deposit
                        print(f"Updated balance: ₹{balance}")
                    elif choice == "3":
                        withdraw = float(input("Enter amount to withdraw: "))
                        if withdraw > balance:
                            print(f"Insufficient funds! Current balance: ₹{balance}")
                        else:
                            balance -= withdraw
                            print(f"Withdrawn ₹{withdraw}. New balance: ₹{balance}")
                    elif choice == "4":
                        print("Exiting the menu...")
                        attempts = 0
                        is_true = False
                        break
                    else:
                        print("Invalid choice, try again.")
                break

            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect password! You have {attempts} attempts left.")
                else:
                    print("You have exceeded the password limit!!!\nLogged out.")
                    is_true = False

    elif is_login.lower() == "n":
        print("Exiting application...")
        break
    else:
        print("Invalid input! Please enter 'y' or 'n'.")