# Example
# Input : 28
# Divisors : [1, 2, 4, 7, 14]
# Sum = 1 + 2 + 4 + 7 + 14 = 28
# Output : It's a Perfect Number


# def Factor(n):
#     divisors = []
#     for i in range(1, n):
#         if n % i == 0:
#             divisors.append(i)
#     return divisors
# n = int(input('Enter the number:'))
# List = Factor(n)
# print(List)
# sum = 0
# for i in List:
#     sum+=i
# if n == sum:
#     print('Its perfect number')
# else:
#     print(' Its not a perfect number!')

n = 28
sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

