def coord(x, y):
    if x >= 1 and y >= 1:
        print('I')
    elif x <= -1 and y >= 1:
        print('II')
    elif x >= 1 and y <= -1:
        print('III')
    elif x <= -1 and y <= -1:
        print('IV')
    else:
        print('Error')

z = int(input('Enter x:'))
w = int(input("Enter y:"))
coord(z, w)