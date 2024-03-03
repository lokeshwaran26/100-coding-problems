a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
hcf = 1
for i in range(1, min(a, b)):
    if a % i == 0 and b % i == 0:
        hcf = i

lcm = (a*b)//hcf
print(lcm)
