x=float(input("Enter X: "))
y=float(input("Enter Y: "))

if(x==0 and y==0 ):
    print("It's the origin!")
elif(x==0 or y==0 ):
    print("One of the coordinates is equal to zero!")
elif (x>0):
    if(y>0):
        print('I')
    else:
        print('IV')
elif (y>0):
        print('II')
else:
    print('III')

