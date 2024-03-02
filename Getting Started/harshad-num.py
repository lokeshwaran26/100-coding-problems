# Example
# Input : 21
# Output : Yes ' It's a Harshad Number.
# Explanation : The sum of the digits of 21 is 3 i.e 2 + 1. As the number 21 is divisible by 3, It's a Harshad Number.
n = int(input('Enter the number:'))
num = str(n)
sum = 0
for i in num:
    sum+=int(i)
if n % sum == 0:
    print("It's Harshad number!")
else:
    print("It's not a Harshad number!")
