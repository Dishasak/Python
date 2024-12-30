# i = 0
# no_of_std = int(input("enter the number of students"))
# while i<= no_of_std :
    
data =input("enter the name of the stuent")
# sub_detail={"python": int(input("enter the marks for python")),"devops": int(input("enter the marks for devops")),"java": int(input("enter the marks for java"))}  
# marks1 = int(input("enter the marks for the python"))
# marks2 = int (input("enter the marks for the devops "))
# marks3 = int(input("enter the java marks"))  

# def __avg__(marks,total):
#     # marks= marks1+marks2+marks3
#     avg = (marks//total)*3   
    
# __avg__(15,30)


 
# print(avg) 

# avgdata ={data:avg}
# print(avgdata)
        # if data not in dict2:
        #     print("enter the data")
        # else:
        #     print({data}, "already present")
   
        # i+=1
        # break
# data.append(sub_detail)
# data1 = data + sub_detail
# data2 =dict(data1)
# print(data2)
# marks1 = int(input("enter the marks for the python"))
# marks2 = int (input("enter the marks for the devops "))
# marks3 = int(input("enter the java marks"))
# avg =(marks1+marks2+marks3//3)
# print(avg)

# dict2 ={data:sub_detail}
# print(dict2)


def avg ():
    total = 3
    marks1 = int(input("enter the marks for the python"))
    marks2 = int (input("enter the marks for the devops "))
    marks3 = int(input("enter the java marks "))
    # marks = marks1+marks2+marks3
    average =(marks1+marks2+marks3)/total
    print("average marks is", average)
    # avg1= dict{average}
    avgdata ={data:{marks1,marks2,marks3,average}}
    print(avgdata)
avg()







