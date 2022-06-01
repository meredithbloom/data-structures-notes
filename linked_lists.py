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
        if target_index > self.get_count():
            return -1
        while target_index != index:
            cur = cur.next 
            index+=1
        print(cur.val)        
        
       
    def get_count(self):
        temp = self.head
        count = 0
        while (temp):
            count+=1
            temp = temp.next 
        return count
        
        
    def list_print(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next 
       
       
    def addAtHead(self, newval):
        NewHead = Node(newval)
        NewHead.next = self.head
        self.head = NewHead 
    
    
    def addAtTail(self, newval):
        NewTail = Node(newval)
        if self.head is None:
            self.head = NewTail
            return
        last = self.head 
        while (last.next):
            last = last.next 
        last.next = NewTail    
         
         
    def InsertAtIndex(self, target_index, newval):
        headval = self.head
        cur_index = 0
        NewNode = Node(newval)
        if target_index > self.get_count():
            print('that index does not exist')
            return
        while headval is not None:
            if cur_index == target_index:
                NewNode.next = headval.next 
                headval.next = NewNode
                return
            else:
                # print('current node is not matching target index. moving to next node')
                headval = headval.next
                cur_index += 1
        
        
    def RemoveAtIndex(self, remove_index):
        if self.head is None:
            return
        if remove_index == 0:
            self.head = self.head.next 
            return self.head
        if remove_index > self.get_count():
            print('invalid index')
            return
        cur = self.head
        prev = self.head 
        temp = self.head
        cur_index = 0
        while cur is not None:
            if cur_index == remove_index:
                temp = cur.next
                break
            prev = cur
            cur = cur.next   
            cur_index += 1
        prev.next = temp
        return prev
         
newlist = SinglyLinkedList()
newlist.head = Node("Mon")
e2 = Node("Tues")
e3 = Node("Wed")

newlist.head.next = e2
e2.next = e3
    

newlist.addAtHead("Sun")
newlist.addAtTail("Thurs")
newlist.addAtTail("Sat")
newlist.InsertAtIndex(4, "Fri")
#newlist.RemoveNode("Fri")
newlist.RemoveAtIndex(5)
#newlist.get_index(2)
# newlist.list_print()
# print(f'the length of newlist is {newlist.get_count()}')



