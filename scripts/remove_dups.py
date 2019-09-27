def removeDup(array):
    final = []
    for l in array:
        if l not in final:
            final.append(l)
    return final

print(removeDup([1,1,2,2,3,3,4,4,5,5]))