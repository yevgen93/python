class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    # ff head is None, return empty list
    if not head:
        return head
    
    current = head
    # Loop thru linked list as long as current's next value is not None
    while current.next:
        # If the current value is the same as the next value
        # set current's next value to be next values "next" aka delete current.next 
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            # continue the loop
            current = current.next
    return head


def createLinkedList(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Create the linked list: 1 -> 1 -> 2 -> 3 -> 3
nums = [1, 1, 2, 3, 3]
head = createLinkedList(nums)

# Print the modified linked list
current = deleteDuplicates(head)
while current:
    print(current.val, end=" -> ")
    current = current.next
