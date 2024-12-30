# fruits=["apple","banana","cherry"]
# print(fruits)
# fruits_tuple = tuple(fruits)
# print(fruits_tuple)
# fruit_color = {"red":"apple","yellow":"banana","green":"cherry"}
# print(fruit_color)
# fruit_color["orange"]="orange"
# print(fruit_color)
# x = fruit_color.pop("orange")
# print(fruit_color)
# x=fruit_color["red"]
# print(x)
# # print(dir(dict))
# y= fruit_color.get("yellow")
# print(y)


# numbers=[2,4,3,5,6]
# print(numbers)
# num_tuple = tuple(numbers)
# print(num_tuple)
# for i in num_tuple:
#     x={i:i*i}
#     print(x)
# x.update({7:49})
# print(num_tuple)


product_id =[101,102,103]
product_id =tuple(product_id)
price = [50,40,20]
details = dict(zip(product_id,price))
print(details)