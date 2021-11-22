score = eval(input("Input Chinese score: "))
score1 = eval(input("Input Chinese score: "))

average = (score + score1)/ 2

if (average >= 80):
    print("excellent!!!")
elif (average >= 70):
    print("good!")
elif (average >= 60):
    print("not bad")
else:
    print("study hard...")

