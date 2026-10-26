budget = float(input("Enter your budget: "))
n = int(input("Enter number of products: "))
if budget < 0 or n < 0:
    print("Invalid input")
else:
    total = 0
    for i in range(n):
         price = float(input("Enter product price: "))
         quantity = int(input("Enter quantity: "))
         if price < 0 or quantity < 0:
                print("Invalid price or quantity")
         else:
              total += price * quantity
    print("Total Bill: Rs.", round(total, 2))
    if total <= budget:
           print("Shopping is within budget")
    else:
       print("Shopping exceeds budget")
       print("Amount to reduce: Rs.", round(total - budget, 2))