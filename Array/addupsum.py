# **********Check the number is equal or no **************
nums = [3,3]
target = 6
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        data = nums[i] + nums[j]
        if data == target:
            print("its equal ")
        else:
            print("its not equal")


# #*************Reverse a integer****************
num = 123
temp = num
rev = 0

while num > 0:
    # print(temp)
    digit = num % 10
    # print(num)
    rev = (rev * 10) +digit
    # print(rev)
    num = num //10
# num+=1 
# print(num)
print(rev)


# # #*******************average world length and print the world contain 5 letter*************
sentence = "hii all,my name is Disha".split()

for i in sentence:
    print(len(i),i)    
    if len(i)==5:
        print(i) 
        

    
    
# #*******************move zero to last************
data =[1,7,0,0,8,0,10,12,0,4]

data1 = [x for x in data if x!= 0]
data2 = [x for x in data if x == 0]
result = data1 + data2
result = sort(result)

print(reversed(result))

# # ***********non-empty array *************


data =[4,4,2,1,3,2,1,4,5]
# data1 = set(data) it display all the items present in the list without duplication
# print(data1)
count = {}  # empty dict because we want ele and the num of occurance so dict...
for i in data:
    count[i] = count.get(i, 0) +1     # gives the ele which is present 1-->if the ele apper once 2-->if the ele apper twice 3--> if the ele apper thrice...
    
    # print("data",count[i])
    # print(data[i])
    
for i,cnt in count.items():
    if cnt == 1:
        print("data that exist only once is: ",i)
        
# #*************count the Frequency****************
nums = [2, 2, 2, 4, 5, 3, 6, 7]

count = {}
for num in nums:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1

most_frequent = None
max_count = 0

for num, freq in count.items():
    if freq > max_count:
        most_frequent = num
        max_count = freq

print(most_frequent)



# ************Happy number*******************
num = 18
sum1 = 0
while num > 9:
    while num > 0:
        d = num % 10
        sum1 = sum1 +(d*d)
        num = num // 10
    num = sum1
    sum1 = 0
if num == 1:
    print("its a happy number")
else:
    print("not a happy number")


# # ************perfect square****************
num = 4  
sq = num**0.5
if num == sq:
    print(f"is a perfect square",int(sq))
else:
    print("not a perfect square")

# ***********above code is not working for perfect square*********

n = int(input("enter the number"))
is_perfect_sqr = False
i = 1
while i*i <= n:
    if i*i == n:
        is_perfect_sqr = True
        break
    i+=1
if is_perfect_sqr:
    print("number is a perfect square")
else:
    print("number is not a perfect square")


#*************reverse with using the inbuilt function*********************
list1 =[1,2,3,4,5,6,7]
list1.reverse()
print(list1)

#*************reverse without using the predefined method*********************

list1 = [1, 2, 3, 4, 5, 6, 7]
i = 0
n = len(list1) - 1
print(n)

while i < n:
    list1[i], list1[n] = list1[n], list1[i]  
    i += 1
    n -= 1  

print(list1)  


#***************smallest in the list************
num =[7, 4, 6, 3, 9, 1]
sortnum=num.sort()
print(num)
print(num[5])



