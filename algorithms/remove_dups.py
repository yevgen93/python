# Allocate new space
def removeDup(arr):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
    return result

# Return the de-duped array in place without allocating new space
# (Assume the input array is sorted)

def removeDupInPlace(arr):
    i = 0
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.pop(i)
        else:
            i += 1
    return arr

print(removeDup([1,1,2,2,3,3,4,4,5,5]))
print(removeDupInPlace([1,1,2,2,3,3,4,4,5,5]))
