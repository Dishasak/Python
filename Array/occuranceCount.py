from array import array

# Create an array
arr = array('i', [10, 20, 30, 20, 40, 50, 20])

# Get the number of occurrences of a specified element
element = 20
occurrences = arr.count(element)

print(f"Element {element} occurs {occurrences} time(s) in the array.")
