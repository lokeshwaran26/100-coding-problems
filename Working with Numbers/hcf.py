a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
hfc = 1
for i in range(1, min(a,b)):
    if a % i == 0 and b % i == 0:
        hfc = i
print(f' The HFC of a and b is {hfc}')