#num = int(input("Input a number(1,3,5 ...): "))

#for i in range(1,num+1):
#    if i%2 == 1:
#        print(i,end =",")
        
n = 5
for i in range(1, 7):
    for j in range(1,i+1):
        print("⏏", end="")
    print()
for i in range(6,0,-1):
    for j in range(1,i+1):
        print("⏏", end="")
    print()
    