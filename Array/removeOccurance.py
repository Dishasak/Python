from array import array

# Create an array
arr = array('i', [10, 20, 30, 20, 40, 50])

# Remove the first occurrence of a specified element
element = 20
if element in arr:
    arr.remove(element)
    print(f"Array after removing the first occurrence of {element}:", arr)
else:
    print(f"Element {element} is not found in the array.")
