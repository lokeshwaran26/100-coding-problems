# Ex:- Take a number:  6
# 6 is a perfect number as 1 + 2 + 3 = 6.
# Ex:- Take a number: 28

# 28 is a perfect number as 1 + 2 + 4 + 7 + 14 = 28
n = int(input('Enter the number:'))
sum = 0
for i in range(1, n):
    if n % i == 0:
        sum+=i
if sum == n:
    print("The number is a Perfect square")
else:
    print("The number is not a Perfect square")
