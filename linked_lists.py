class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def list_print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next 
       
       
         

newlist = SinglyLinkedList()
newlist.head = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")

newlist.head.next = e2
e2.next = e3

newlist.list_print()        