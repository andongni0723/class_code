sum = 0
num = int(input("input the 'N'(1+2+...N):"))

for i in range(1,num+1):
    sum += i
print("1+2+...{}={}" .format(num, sum))