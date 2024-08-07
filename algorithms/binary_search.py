# Take a sorted array
# Return the index of the target value found, or -1 if not found

def binary_search(array, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle = (left + right) // 2

        if nums[middle] > target:
            right = middle - 1
            
        elif nums[middle] < target:
            left = middle + 1
            
        else:
            return middle
            
    return -1

sorted_array = [1,3,5,7,9,11,13]
target_value = 7

result = binary_search(sorted_array, target_value)

if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the array")
