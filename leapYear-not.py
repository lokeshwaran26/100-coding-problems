year = int(input('Enter the Number:'))
if year % 400 == 0 or ( year % 4 == 0 and year%100 != 0):
    print('Leap year')
else:
    print("Not leap year")