class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
     
        
    def get_index(self, target_index):
        index = 0
        cur = self.head
        while target_index != index:
            cur = cur.next 
            index+=1
        print(cur.val)        
        
        
    def list_print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next 
       
       
    def AtBegining(self, newval):
        NewHead = Node(newval)
        NewHead.next = self.head
        self.head = NewHead 
    
    
    def AtTail(self, newval):
        NewTail = Node(newval)
        if self.head is None:
            self.head = NewTail
            return
        last = self.head 
        while (last.next):
            last = last.next 
        last.next = NewTail    
         
         
    def InsertBetween(self, middle_node, newval):
        if middle_node is None:
            print("the mentioned node is absent")
            return
        NewNode = Node(newval)
        NewNode.next = middle_node.next 
        middle_node.next = NewNode
       
        
    def RemoveNode(self, RemoveKey):
        headval = self.head 
        if headval is not None:
            if headval.val == RemoveKey:
                self.head = headval.next 
                headval = None 
                return 
        while headval is not None:
            if headval.val == RemoveKey:
                break
            prev = headval
            headval = headval.next
        if headval == None:
            return
        prev.next = headval.next 
        headval = None        
        
        

newlist = SinglyLinkedList()
newlist.head = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")


newlist.head.next = e2
e2.next = e3


#newlist.list_print()        

newlist.AtBegining("Sun")
newlist.AtTail("Thurs")
newlist.AtTail("Sat")
newlist.InsertBetween(newlist.head.next, "Fri")
newlist.RemoveNode("Fri")
newlist.list_print()
#newlist.get_index(2)