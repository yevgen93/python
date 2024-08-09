# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of the new sorted linked list.
# The new list should be made up of nodes from list1 and list2.

# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]

# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]

# Example 3:
# Input: list1 = [], list2 = []
# Output: []

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
      dummy = ListNode()   # Placeholder node
      tail = dummy         # Pointer to to keep track of where to append new nodes and build the merged list

      while l1 and l2:
          if l1.val < l2.val:
              tail.next = l1
              l1 = l1.next
          else:
              tail.next = l2
              l2 = l2.next
          tail = tail.next     # Move tail to the new end of the merged list

      # If either list is still not None, append it to the tail
      if l1:
          tail.next = l1
      elif l2:
          tail.next = l2
      
      return dummy.next       # Return the actual head of the merged list
