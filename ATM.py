# 1. Createing an ATM program:
def ATM():

# 2. Creating an User Authentication like Acc. No and PIN:
    user_account_no = 123456789012
    user_pin = 000000
    balance = 1000.00

    account = int(input("Account Number: "))
    pin = int(input("Enter PIN: "))

    if account == user_account_no and pin == user_pin:
        while True:
            print("Choose the following options:\n1. Balance Inquiry\n2. Withdraw\n3. Cancel Transaction")
            choice = int(input("Enter choice (1/2/3): "))

            if choice == 1:
                print("Current Balance", balance)
            elif choice == 2:
                if balance == 0:
                    print("You have 0 Balance Left. Returning to Menu.")
                else:
                    while True:
                        amount = float(input("Enter Withdrawal Amount: "))
                        if amount <= 0:
                            print("Must be greater than 0. Try Again")
                        elif amount > balance:
                            print("Insufficient Funds! Try Again. Your Balance:", balance)
                        elif amount <= balance:
                            print("Processing...")
                            old = balance
                            balance -= amount
                            print("----Transaction Receipt----")
                            print("Balance:", old)
                            print("Amount Withdrawn:", amount)
                            print("New Balance", balance)
                            print("---------------------------")
                            break
                        else:
                            print("Invalid Input. Must be a Number")
            elif choice == 3:
                print("Cancelling Transaction. Please Wait...")
                print("Transaction Cancelled. Exiting...")
                break
            else:
                print("Invalid Option. Try again. Must be 1/2/3+")
            
            while True:
                again = input("Another Transaction? (y/n): ").lower()
                if again == "y":
                    print("Processing. Please Wait...")
                    break
                elif again == "n":
                    print("Thank You. Exiting...")
                    return
                else:
                    print("Invalid Input. Must be y or n")
    else:
        print("Authentication Failed or Invalid. Re-run the program.")
        print("Exiting...")
ATM()