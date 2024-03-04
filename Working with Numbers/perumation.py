def fact(n):
    sum = 1
    for i in range(1, n+1):
        sum*=i
    return sum


n = int(input('Enter the number:'))
r = int(input('Enter the number:'))

val = fact(n)//fact(n-r)
print(val)