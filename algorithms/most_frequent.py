# Given an array, find the most frequently occuring num.
# array = [1,3,3,3,2,1,1,1]
# most_frequent(array) should return 1



def mostFrequent(arr):
    map = {}
    most_frequent_count = 0
    most_frequent_num = None

    # Count occurence of each num where
    # current_frequent_count = map[num]
    for num in arr:
        if num in map.keys():
            map[num] += 1
        else:
            map[num] = 1
    # Check current num frequency against most_frequent_count
        if map[num] > most_frequent_count:
            most_frequent_count = map[num]
            most_frequent_num = num
    return most_frequent_num

print(mostFrequent([1,3,3,3,2,1,1,1])) # 1
print(mostFrequent([1,3,3,3,2,1,1])) # 3
print(mostFrequent([1,2,2,3])) # 2
