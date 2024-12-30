# #list to dict conversion:::

# list_data = [
#     ("id", 1, "name", "Alice"),
#     ("id", 2, "name", "Bob"),
# ]

# dict_data = {
#     "user3": ("id", 3, "name", "Charlie"),
#     "user4": ("id", 4, "name", "David"),
# }

# extra_list = [{"id": 5, "name": "Eve"}]

# result = list_data+[dict_data]+extra_list
# print(result)


# data = [("id", 1, "name", "Alice"), ("id", 2, "name", "Bob")]
# result =[]


# for items in data:
#     temp_dict ={}
#     for i in range(0, len(items),2):
#         key =items[i]
#         value =items[i+1]
#         temp_dict[key] = value
#         result.append(temp_dict)
# print(result)

#*****************************************************


#find the unique value and store it in the set
# data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}, {"id": 1, "name": "Alice"}]

# seen_ids = set()
# unique_data = []

# for item in data:
#     if item["id"] not in seen_ids:
#         unique_data.append(item)
#         seen_ids.add(item["id"])

# print(unique_data)


# Merge and delete duplicate:
# Combine the following data into a single list of dictionaries without duplicate id values:
# list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# list2 = [{"id": 2, "name": "Robert"}, {"id": 3, "name": "Charlie"}]
# # list1= dict(list1)
# # list2= dict(list2)
# result = list1+list2
# new_Set = set()
# duplic = []
# for items in result:
#     if items["id"] not in duplic:
#         duplic.append(items)
#         new_Set.add(items["id"])
# print(duplic)
        
# Input : data = {('Math', 'Alice'): 85, ('Science', 'Bob'): 78, ('Math', 'Charlie'): 95, ('Science', 'Alice'): 92}
# Output : {'Alice': {'Math': 85, 'Science': 92}, 'Bob': {'Science': 78}, 'Charlie': {'Math': 95}}

# data = {('Math', 'Alice'): 85, ('Science', 'Bob'): 78, ('Math', 'Charlie'): 95, ('Science', 'Alice'): 92}
# print(data)
# output={}
# for (sub,name), score in data.items():
#     if name not in output:
#         output[name]={}
#     output[name][sub]=score
# print(output)


# students = {
#     "Alice": {"age": 25, "subjects": ["Math", "Physics"]},
#     "Bob": {"age": 22, "subjects": ["Chemistry", "Biology"]},
#     "Charlie": {"age": 23, "subjects": ["History", "Geography"]}
# }

# students.update({"David": {"age":26,"subjects":["English","Frech"]}})
# print(students)

# students.update({"Charlie": {"age":34}})
# print(students)

# students.pop("Bob")
# print(students)


# keys = ["id", "name", "age"]
# values = [1, "Alice", 25]
# # keys= dict(keys)
# # values =dict(values)
# person = dict(zip(keys, values))
# print(person)
# person["city"] = "newyork"
# print(person)
# person=list(person)
# print(person)



# keys =["name","age","email"]
# values =["John",23,"john@email"]
# items1 = dict(zip(keys, values))
# print(items1)
# items1["city"] = "neywork"
# print(items1)


# ele = ["a","b","c","d"]
# nested = None


# for items in reversed(ele):
#     nested={items: nested}

# print(nested)


# studentmarks ={"alice":85,
#                "bob": 54,
#                "charlie": 47} 
# print(studentmarks["bob"])
    
    
# lst =[(1, 'a'), (2, 'b'), (3, 'c')]
# lst1 = dict(lst)
# print(lst1)
# for key,value in lst1.items():
#     # key = list[key]
#     print([key],(value))
#     # print(value)

# lst=[['name', 'John'], ['age', 25], ['city', 'New York']]

# lst1=dict(lst)
# print(lst1)


lst=['apple', 'banana', 'cherry']
for x in range(0, len(lst)):
    print(x)
for y in lst:
    print(y)
    print(len(y))
print(f"{y:[x ,len(y)]}")
print(z)
