even_no=0
odd_no=0
n1=(1,2,3,4,5,6,7,8,9)

for x in n1:
    if x%2==0:
        even_no+=1
    else:
        odd_no+=1
print("number of even number is",even_no)
print("number of odd number is",odd_no)
