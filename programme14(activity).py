products = ["Pens", "Books", "Pencils"]
opening = [100, 50, 80]
incoming = [20, 10, 30]
dispatched = [40, 25, 50]
for i in range(len(products)):
     closing = opening[i] + incoming[i] - dispatched[i]
     print("Product:", products[i])
     print("Closing Stock:", closing)
     if closing < 20:
          print("Status: Reorder required")
     else:
          print("Status: Stock sufficient")