# #adding in the data

# # data ={}

# # key1= input("enter the key")
# # value1= input("enter the value")
# # print("data added sucessfully")
# # data[key1]=value1
# # print (data)



# #*********************************



# data = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# key = input("Enter the key to delete: ")
# if key in data:
#     del data[key]
#     print("Key deleted. Updated Dictionary:", data)
# else:
#     print("Key not found!")
    
    
# #*******************************
# #  Check for Key Existence

# data = {"name": "Alice", "age": 25, "city": "New York"}

# key = input("Enter key to check: ")
# if key in data:
#     print(f"'{key}' exists in the dictionary with value: {data[key]}")
# else:
#     print(f"'{key}' does not exist in the dictionary.")
    
    
# #**********************************
# # Update a value
# data = {"a": 1, "b": 2, "c": 3}

# # Update a value
# key = input("Enter key to update: ")
# if key in data:
#     new_value = input(f"Enter new value for '{key}': ")
#     data[key] = new_value
#     print("Value updated. Dictionary:", data)
# else:
#     print("Key not found!")
    
    
    
# #******************************
# # Count word frequencies
# text = input("Enter a string: ")

# words = text.split()
# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# # Display word frequencies
# print("Word Frequencies:", word_count)


# #***********************************
# # Merge Two Dictionaries
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# merged_dict = {**dict1, **dict2}

# print("Merged Dictionary:", merged_dict)


# #********************************
# # Initialize a dictionary
# data = {"a": 10, "b": 20, "c": 15}


# #******************************************
# # Find the key with the maximum value
# max_key = max(data, key=data.get)
# print(f"Key with maximum value: '{max_key}' (Value: {data[max_key]})")

# #******************************************
# #swap the dict
# data = {"a": 1, "b": 2, "c": 3}

# swapped_dict = {value: key for key, value in data.items()}

# print("Swapped Dictionary:", swapped_dict)

# #******************************************
# # Display all keys and values
# data = {"name": "Alice", "age": 25, "city": "New York"}

# print("Dictionary Contents:")
# for key, value in data.items():
#     print(f"Key: {key}, Value: {value}")

# #******************************************
# # store and retrivew student grade
# students = {}

# name = input("Enter student name: ")
# grades = input("Enter grades separated by space: ").split()

# # Convert grades to floats manually
# grades_float = []
# for grade in grades:
#     grades_float.append(float(grade))

# students[name] = grades_float

# # Retrieve grades
# search_name = input("Enter student name to retrieve grades: ")
# if search_name in students:
#     print(f"Grades for {search_name}: {students[search_name]}")
# else:
#     print("Student not found!")


# #******************************************

