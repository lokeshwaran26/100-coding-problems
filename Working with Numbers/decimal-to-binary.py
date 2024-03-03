n = int(input('Enter the number:'))
num = n
binary = 0
i = 1
while num != 0:
    rem = num % 2
    num //= 2
    binary += rem*i
    i *= 10
print(binary)
