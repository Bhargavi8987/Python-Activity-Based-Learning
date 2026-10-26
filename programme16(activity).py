level = 500
capacity = 1000
days = int(input("Enter number of days: "))
if days < 0:
    print("Invalid number of days")
else:
   for i in range(days):
       inflow = int(input("Enter water inflow: "))
       outflow = int(input("Enter water outflow: "))
       if inflow < 0 or outflow < 0:
             print("Invalid inflow/outflow")
             continue
       level = level + inflow - outflow
       if level > capacity:
            level = capacity
            print("Overflow detected")
       if level < 0:
            level = 0
            print("Water shortage detected")
       print("Day", i + 1, "Water Level:", level)