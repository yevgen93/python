# def removeDup(array):
#     final = []
#     for l in array:
#         if l not in final:
#             final.append(l)
#     return final

# print(removeDup([1,1,2,2,3,3,4,4,5,5]))

# assume the input array is sorted
# return the de-duped array in place

def removeDup(array):
    i = 0
    while i<len(array)-1:
        if array[i]==array[i+1]:
            array.pop(i)
        else:
            i+=1
    return array

print(removeDup([1,1,2,2,3,3,4,4,5,5,6]))
