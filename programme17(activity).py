subjects = ["Python", "Maths", "English"]
for subject in subjects:
     first = int(input("Enter first exam marks for " + subject + ": "))
     second = int(input("Enter second exam marks for " + subject + ": "))
     print(subject)
     if second > first:
         print("Performance improved")
     elif second < first:
         print("Performance declined")
     else:
         print("Performance unchanged")