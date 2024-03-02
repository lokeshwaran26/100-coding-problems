def factorial(n):
    num =  1
    for i in range(1, n+1):
        num*=i
    return num
n = int(input('Enter the number:'))
result = factorial(n)
print(result)