# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val,
# and return the new head.
# Example 1:
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeElements(head, val):
    # Create a dummy node that points to the head
    dummy = ListNode(0)
    dummy.next = head
    
    # Initialize current node to the dummy node
    curr = dummy
    
    while curr and curr.next:
        if curr.next.val == val:
            # Skip the node with the value to be removed
            curr.next = curr.next.next
        else:
            # Move to the next node
            curr = curr.next
    
    # Return the new head which is the next of the dummy node
    return dummy.next
