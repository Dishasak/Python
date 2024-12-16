import array

#Creating array
arr = array.array('i', [1, 2, 3, 4])
print(arr)


#inserting(Replacing) elememt in an array
arr[1]=10
print(arr)

#accessing element in an array
print(arr[2])
print(arr[-1])


#inserting element in array
arr.append(5)
print(arr)
arr.extend([6,7,8])
print(arr)

#removing element in array  .. By the element itself
arr.remove(7)
print(arr)

#rempving element in array  .. By the index of the element
arr.pop(2)
print(arr)

#Looping through the loop
for i in arr:
    print(i,end =",")





