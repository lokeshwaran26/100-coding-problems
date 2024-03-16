def prim(n):
    count = 0
    if n < 2:
        return False
    else:
        for i in range(2, n//2):
            if n % i == 0:
                return False
    return True

for i in range(2, 100):
    result = prim(i)
    if result == True:
        print(i, end=' ')
      