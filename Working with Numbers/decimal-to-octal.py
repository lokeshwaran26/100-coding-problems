n = int(input('Enter the number:'))
num = n
octal = 0
i = 1
while num != 0:
    rem = num % 8
    num //= 8
    octal += rem*i
    i *= 10
print(octal)
