n = int(input("Input a number: "))

# low to high
for i in range(1,n+1):
    for j in range(1,i+1):
        print("{}" .format(j), end="")
    print()
    
print()

# high to low
for i in range(n,1,-1):
    for j in range(1,i+1):
        print("{}" .format(j), end="")
    print()