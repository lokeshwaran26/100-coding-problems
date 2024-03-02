# Example
# Input : 145
# Output : It's a Strong Number.
# Explanation : Number = 145
# 145 = 1! + 4! + 5!
# 145 = 1 + 24 + 120

def fact(n):
    if n == 1 or n==0:
        return 1
    pw = 1
    for i in range(1,n+1):
        pw = pw * i
    return pw
n = int(input('Enter the number:'))
val = n
sum = 0
while(n!=0):
    mod = n % 10
    num = fact(mod)
    sum+=num
    n//=10
print(sum)
if sum == val:
    print(f'{val} is strong number')
else:
    print(f'{val} is not strong number')
