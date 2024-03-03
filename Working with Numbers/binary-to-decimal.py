n = int(input('Enter the number:'))
num = n
dec = 0
base = 1
while num > 0:
    rem = num % 10
    dec = dec + rem*base
    num = num//10
    base*=2
print(dec)