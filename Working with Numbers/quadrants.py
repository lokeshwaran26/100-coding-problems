x = int(input('Enter the number:'))
y = int(input('Enter the number:'))

if ( x>0 and y>0 ):
    print('First Quadrant')
elif ( x<0 and y>0 ):
    print('Second Quadrant')
elif ( x<0 and y<0 ):
    print('Third Quadrant')
elif ( x>0 and y>0 ):
    print('Fourth Quadrant')
elif ( x==0 and y==0 ):
    print('Origin')
elif ( x!=0 and y==0 ):
    print('x-axis')
else:
    print('y-axis')