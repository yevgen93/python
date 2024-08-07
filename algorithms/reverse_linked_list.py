# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode):
    prev = None
    curr = head
    
    while curr:
        tmp = curr.next      # Store next node
        curr.next = prev      # Reverse the link
        prev = curr           # Move prev forward
        curr = tmp            # Move current forward
    return prev  
