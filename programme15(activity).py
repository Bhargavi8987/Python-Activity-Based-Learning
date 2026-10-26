hours = int(input("Enter parking hours: "))
if hours <= 0:
   print("Invalid parking duration")
else:
    if hours <= 2:
        fee = hours * 20
    else:
        fee = 40 + (hours - 2) * 10
    if fee > 150:
         fee = 150
    print("Parking Fee: Rs.", fee)