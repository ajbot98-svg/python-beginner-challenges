# Home Work from GPT
# Challenge_4
# ATM Machine Simulation

print ("Welcome to the ATM Machine")
balance = 1000.0

print ("ATM MENU")
print ("1. Check Balance")
print ("2. Deposit Money")
print ("3. Withdraw Money")
print ("4. Exit")

choice = input("enter your choice: ")

if choice == '1':
    print (f"your balance is: {balance}")
elif choice == '2':
    amount = float(input("Enter amount to diposist: "))
    balance += amount
    print (f"Deposit successful! Your new balance: {balance}")
elif choice == '3':
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance -= amount
        print (f"Withdrawal successful! your new balance: {balance}")
    else:
        print ("Insufficient funds!")
elif choice == '4':
    print ("Thank you for using the ATM. Goodbye!")