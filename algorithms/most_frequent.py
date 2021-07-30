# Given an array, what is the most frequently occuring element?
# array = [1,3,3,3,2,1,1,1]
# most_frequent(array) should return 1


def most_frequent(list):
  d = {}
  max_count = 0
  max_item = 0
  
  for item in list:
    if item not in d:
      # set the count of this item
      d[item] = 1
    else:
      d[item] += 1
    
    if d[item] > max_count:
      max_count = d[item]
      max_item = item
   
  return max_item
  
