arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month = 12
year = 2012

if (month == 2 and ((year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)))):
    print("Number of days is ", arr[month-1]+1)

else:
    print("Number of days is ", arr[month-1])
