# We have to find the common integers in both lists

# print(intersecting_elements({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}))
# # Expected output: [10, 9, 8, 7, 6, 5]

# print(intersecting_elements({-1, -2, -3, -4, -5}, {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}))
# # Expected output: [-1, -2, -3, -4, -5]

# print(intersecting_elements({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}))
# # Expected output: []

def intersecting_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return sorted(list(set1 & set2), reverse=True)
