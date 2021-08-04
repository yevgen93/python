# Implement a queue (first-in-first-out) data structure with the following operations: enqueue, dequeue, and get, 
# which can be used to
# fetch the nth element without removing it from the queue.
# 
# - all 3 operations happen in amortized O(1) time
# - think about what data structures can support constant time lookups

# key = position
# value = element

position, start = 0,0 

# return the element (value) at the position (key)
def get(d, position):
    return d[position]


# add element to the end of the hashmap, increment position by 1
def enqueue(d, element):
    global position
    d[position] = element
    position += 1
    
# delete the first element of the hashmap, FIFO, and return it
def dequeue(d):
    global start
    final = d[start]
    del(d[start])
    return final

    
d = {}

enqueue(d, 5)
enqueue(d, 6)
enqueue(d, 7)
print(d)
dequeue(d)
print(d)
    
