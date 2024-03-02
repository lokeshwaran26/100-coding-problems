def printDivisors(n):
    i = 1
    sum = 0
    while i <= n:
        if (n % i == 0):
            sum+=i
        i = i + 1
    return sum
a = 6
b = 28
val1 = printDivisors(a)
val2 = printDivisors(b)
if val1 % a == 0 and val2 % b == 0:
    print("It's a Friendly pair")
else:
    print("It's not a Friendly pair")
