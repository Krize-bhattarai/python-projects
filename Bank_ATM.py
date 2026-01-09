# FULL ATM PROGRAM


balance = 15000
correct_pin = '1234'
max_pin_attempts = 3

print("Welcome to CBA [Commonwealth Bank ATM]")

# --- PIN verification (max 3 attempts TOTAL) ---
pin_attempts = 0
while pin_attempts < max_pin_attempts:
    pin = input("Please enter your 4-digit PIN: ")
    pin_attempts += 1  # COUNT EVERY ATTEMPT

    if not pin.isdigit():
        print("Error: PIN must be numbers only.")
    elif pin == correct_pin:
        print("PIN accepted. You can access your account.")
        break
    else:
        print("Incorrect PIN.")

    print(f"Attempts left: {max_pin_attempts - pin_attempts}")

else:
    print("Too many incorrect PIN attempts. Your account is locked.")
    exit()

# --- ATM operations ---
max_invalid_attempts = 3
invalid_attempts = 0

while True:
    print("\nHow can I help you?")
    print('1. Check Balance')
    print('2. Deposit Amount')
    print('3. Withdraw Amount')
    print('4. Close Program')
    
    choice = input('Enter your choice (1-4): ')
    
    # --- Validate menu input ---
    if not choice.isdigit() or int(choice) not in range(1, 5):
        invalid_attempts += 1
        print(f"Invalid entry. Attempt {invalid_attempts} of {max_invalid_attempts}")
        
        if invalid_attempts >= max_invalid_attempts:
            print("Too many invalid attempts. Your account is locked.")
            break
        
        # Ask if user wants to continue
        while True:
            cont = input("Do you want to continue? (y/n): ").lower()
            if cont == 'y':
                break
            elif cont == 'n':
                print("Thank you. Goodbye!")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        continue
    
    choice = int(choice)
    invalid_attempts = 0  # reset after valid entry
    
    # --- ATM operations ---
    if choice == 1:
        print(f'Your current balance is: ${balance}')
        receipt = input("Would you like a receipt? (y/n): ").lower()
        if receipt == 'y':
            print(
                "--- RECEIPT ---\n"
                f"Balance: ${balance}\n"
                "Thank you for using CBA ATM\n"
                "----------------"
            )
    
    elif choice == 2:
        try:
            deposit_amount = float(input("Enter amount to deposit: $"))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"Deposit successful! Your new balance is ${balance}")
                receipt = input("Would you like a receipt? (y/n): ").lower()
                if receipt == 'y':
                    print(
                        "--- RECEIPT ---\n"
                        f"Deposited: ${deposit_amount}\n"
                        f"Balance: ${balance}\n"
                        "Thank you!\n"
                        "----------------"
                    )
            else:
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount entered. Please enter numbers only.")
    
    elif choice == 3:
        try:
            withdraw_amount = float(input("Enter amount to withdraw: $"))
            if withdraw_amount > 0:
                if balance >= withdraw_amount:
                    balance -= withdraw_amount
                    print(f"Withdrawal successful! Your new balance is ${balance}")
                    receipt = input("Would you like a receipt? (y/n): ").lower()
                    if receipt == 'y':
                        print(
                            "--- RECEIPT ---\n"
                            f"Withdrawn: ${withdraw_amount}\n"
                            f"Balance: ${balance}\n"
                            "Thank you!\n"
                            "----------------"
                        )
                else:
                    print("Insufficient balance.")
            else:
                print("Withdrawal amount must be positive.")
        except ValueError:
            print("Invalid amount entered. Please enter numbers only.")
    
    elif choice == 4:
        print("Thank you for using CBA ATM. Goodbye!")
        break
