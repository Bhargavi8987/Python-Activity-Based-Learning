marks = []
n = int(input("Enter number of subjects: "))
for i in range(n):
   m = int(input("Enter marks out of 100: "))
   marks.append(m)
for i in range(len(marks)):
    if 30 <= marks[i] < 35:
        marks[i] = min(100, marks[i] + 5)
total = sum(marks)
print("Final Marks:", marks)
print("Total Marks:", total)
if all(m >= 35 for m in marks):
        print("Result: Pass")
else:
    print("Result: Fail")