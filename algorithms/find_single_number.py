def find_single_number(array):
    d = {}

    for num in array:
        if num in d.keys():
            d[num] += 1
        else:
            d[num] = 1
    
    for num, freq in d.items():
        if freq == 1:
            return num

array = [1, 1, 2, 2, 6, 3, 3, 4, 4]
single_number = find_single_number(array)
print(single_number)
