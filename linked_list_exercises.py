class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



# testing if linked list has cycle using "floyd's cycle finding algo"

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next 
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next 
            fast = fast.next.next 
        return True
