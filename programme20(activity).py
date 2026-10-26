candidates = []
n = int(input("Enter number of candidates: "))
for i in range(n):
    name = input("Enter candidate name: ")
    marks = int(input("Enter aggregate marks out of 100: "))
    subject = int(input("Enter required subject marks: "))
    if marks >= 70 and subject >= 60:
        candidates.append((name, marks))
candidates.sort(key=lambda x: x[1], reverse=True)
print("\nEligible Candidates Ranked by Marks:")
if len(candidates) == 0:
    print("No eligible candidates")
else:
    for rank, candidate in enumerate(candidates, start=1):
        print(rank, candidate[0], "-", candidate[1])