def PrimeN(n):
    count = 0
    for i in range(2, n // 2):
        if n % i == 0:
            count += 1
            break
        if count == 0:
            return True #print("Prime")
        else:
            return False #print("Not prime")
        
num1, num2 = 41, 56
num = ''
for i in range(num1, num2+1):
    if PrimeN(i):
        num += str(i) +' '
print(num)
    
