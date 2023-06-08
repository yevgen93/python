# Split array
# Given an array of integers greater than zero, find if it is possible to split 
# it in two subarrays, such that the sum of the two subarrays is the same. Print the two subarrays.
# You cannot reorder the initial array.

# Examples:
# [1,2,3,3,1,1,1] -> [1,2,3] [3,1,1,1]
# [1,5,4,3,6,1] -> [1,5,4] [3,6,1]


def split(array):
    # Duplicate the original array so that it doesn't
    # get modified with the .pop() method
    dupArray = array[:]
    halfTotalSumOfArray = sum(array)/2
    rightSum, rightArray  = 0, []
    # Keep popping off the last number from the dup'd array
    # and adding it to the array being returned
    while(rightSum < halfTotalSumOfArray):
        lastNum = dupArray.pop()
        rightSum += lastNum
        rightArray.append(lastNum)
    return rightArray, dupArray

print(split([1,2,3,3,1,1,1]))
print(split([1,5,4,3,6,1]))
