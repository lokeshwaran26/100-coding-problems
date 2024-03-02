n = int(input('Enter the number:'))
num = n
i = 2
val = ''
while( num > 1):
    while(num % i == 0):
        # val += str(i)+ ' '
        print(i, end=' ')
        num = num / i
    i+=1
        
print(val)