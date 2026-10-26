balance = 1000
n = int(input("Enter number of transactions: "))
for i in range(n):
    print("1. Deposit")
    print("2. Withdraw")
    choice = int(input("Enter your choice: "))
    amount = float(input("Enter amount: "))
    if amount <= 0:
       print("Invalid amount")
    elif choice == 1:
        balance += amount
        print("Deposit successful")
    elif choice == 2:
         if amount <= balance and amount <= 5000:
              balance -= amount
              print("Withdrawal successful")
         else:
             print("Insufficient balance or limit exceeded")
    else:
        print("Invalid choice")
print("Final Balance:", balance)
