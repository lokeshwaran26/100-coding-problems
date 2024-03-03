n = int(input('Enter the number:'))
num = n
pwr = 0
dec = 0
while num!=0:
    mod = num % 10
    ans = mod*(8**pwr)
    dec+=ans
    pwr+=1
    num//=10
print(dec)