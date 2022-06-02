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


    # use hash table to find linked node index
    def detectCycle(self, head: ListNode) -> ListNode:
        # initialize a set. unordered, unindexed, unchangeable (items only)
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node 
            else:
                visited.add(node)
                node = node.next 
        return None
        
        

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        prev = None
        current = head
        while current is not None:
            next = current.next 
            current.next = prev
            prev =current
            current = next
        head = prev
        return head

            
    def removeElements(self, head: Optional[ListNode], val):
        sentinel = ListNode(0)
        sentinel.next = head
        prev, curr = sentinel, head
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sentinel.next




