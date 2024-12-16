noOfStudents = int(input("Enter the number of students going for the trip "))
noOfTeachers = int(input("Enter the number of students going for the trip "))

total_participents = noOfStudents + noOfTeachers

print("Toal num of participents for the trip is ", total_participents)

large_bus = total_participents // 46
print("The number of large buses is",large_bus)

remainder = total_participents%46 # remaning people

small_bus = remainder //16
#print("The number of small buses is",small_bus)

remainder = total_participents% 16


if (remainder>0):
    small_bus =small_bus+1
    print("number of small buses is ", small_bus)


total_cost = large_bus * 360 + small_bus * 140

print("The total cost of the bus trip is ",total_cost)



