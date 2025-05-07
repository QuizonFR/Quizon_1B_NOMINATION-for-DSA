# 1. Createing an ATM program:
# Function
def ATM():

# 2. Creating an User Authentication like Acc. No and PIN:
    # Valid Acc No. and PIN
    user_account_no = 123456789012
    user_pin = 000000
    balance = 1000.00
    # User prompt Acc. No. and PIN
    account = int(input("Account Number: "))
    pin = int(input("Enter PIN: "))
    # Condition weather if the given prompt is true or false
    if account == user_account_no and pin == user_pin:
        while True:
            # 3. Program asks the options:
            print("Choose the following options:\n1. Balance Inquiry\n2. Withdraw\n3. Cancel Transaction")
            choice = int(input("Enter choice (1/2/3): "))
            # 3.1. Balace Inquiry option
            if choice == 1:
                print("Current Balance", balance)
            # 3.2. Withdraw Cash option
            elif choice == 2:
                if balance == 0: # if the balance is ran out or 0
                    print("You have 0 Balance Left. Returning to Menu.")
                else:
                    while True: 
                        amount = float(input("Enter Withdrawal Amount: ")) # ask the amount to withdraw
                        if amount <= 0:
                            print("Must be greater than 0. Try Again") # if below 0
                        elif amount > balance:
                            print("Insufficient Funds! Try Again. Your Balance:", balance) # if more withdrawal amount than current balance
                        elif amount <= balance:
                            print("Processing...") # Show processing...
                            old = balance
                            balance -= amount
                            print("----Transaction Receipt----") # Receipt Info of Withdrawal
                            print("Balance:", old) # Balance
                            print("Amount Withdrawn:", amount) # Withdraw Amt
                            print("New Balance", balance) # New Balance
                            print("---------------------------")
                            break
                        else:
                            print("Invalid Input. Must be a Number")
            # 3.3 Cancel Transaction option
            else:
                print("Cancelling Transaction. Please Wait...")
                print("Transaction Cancelled. Exiting...")
                break
            # Ask for Another Transaction
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
    # if user input invalid:
    else:
        print("Authentication Failed or Invalid. Re-run the program.")
        print("Exiting...")
ATM() # Call a function
