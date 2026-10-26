distance = float(input("Enter journey distance in km: "))
mileage = float(input("Enter vehicle mileage in km per litre: "))
price = float(input("Enter fuel price per litre: "))
if distance <= 0 or mileage <= 0 or price < 0:
      print("Invalid input")
else:
   fuel = distance / mileage
   cost = fuel * price
   print("Fuel Required:", round(fuel, 2), "litres")
   print("Journey Cost: Rs.", round(cost, 2))