x = input("enter the first side ")
y = input ("enter the second side ")
z = input("enter the third side ")


if(x==y and x ==z and y == z):
    print("its a equilteral triangle")
elif(x!= y and y != z and x!=z):
    print("its a scalene triangle")
elif(x==y or y==z or x==z):
    print('its a isoscalene triangle')