n =int(input('Enter the number:'))
num = n
sum = 0
pwr = len(str(n))
while n!=0:
    mod = int(n % 10)
    val = mod**pwr
    sum+=val
    n = n / 10
print(sum)
if (sum == num):
    print("It is armstrong")
else:
    print('It is not armstrong number')

