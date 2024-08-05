# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# You may return the output in any order.
# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]


def topKFrequent(nums,k):
       # Step 1: Count the frequency of each element
        frequency_map = {}
        for element in nums:
            if element in frequency_map:
                frequency_map[element] += 1
            else:
                frequency_map[element] = 1
    
        # Step 2: Create a list of tuples (element, frequency)
        items = list(frequency_map.items())
    
        # Step 3: Sort the list of tuples by frequency in descending order
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    
        # Step 4: Extract the top k elements
        top_k_elements = []
        for i in range(k):
            top_k_elements.append(sorted_items[i][0])
    
        return top_k_elements
