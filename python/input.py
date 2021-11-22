name = input("Input classmate name: ")
score = eval(input("Input classmate score: "))

name2 = input("Input second classmate name: ")
score2 = eval(input("Input second classmate score: "))

print("{}'s score is {}" .format(name, score))
print("{}'s score is {}" .format(name2, score2))
print("{}'s score add {}'s score is {}" .format(name, name2, score + score2))