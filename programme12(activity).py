held = int(input("Enter total classes held: "))
attended = int(input("Enter classes attended: "))
if held <= 0 or attended < 0 or attended > held:
    print("Invalid attendance data")
else:
    percentage = attended / held * 100
    print("Attendance Percentage:", round(percentage, 2), "%")
    classes = 0
    while percentage < 75:
         attended += 1
         held += 1
         classes += 1
         percentage = attended / held * 100
    print("Additional classes required:", classes)
    print("Final Attendance:", round(percentage, 2), "%")