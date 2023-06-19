# Take a sorted array
# Return the index of the target value found, or -1 if not found

def binary_search(array, target):
    left_index = 0
    right_index = len(array)-1

    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2

        if array[middle_index] == target:
            return middle_index
        
        if array[middle_index] < target:
            left_index = middle_index + 1
        else:
            right_index = middle_index - 1
    
    return -1 # Target not found

sorted_array = [1,3,5,7,9,11,13]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the array")
