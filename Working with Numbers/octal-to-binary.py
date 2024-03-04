# Convert octal to decimal and then decimal to binary
n = int(input('Enter the number:'))
num = n
pwr = 0
dec = 0
while num != 0:
    mod = num % 10
    ans = mod*(8**pwr)
    dec += ans
    pwr += 1
    num //= 10
print(dec)

num = dec
binary = 0
i = 1
while num != 0:
    rem = num % 2
    num //= 2
    binary += rem*i
    i *= 10
print(binary)
