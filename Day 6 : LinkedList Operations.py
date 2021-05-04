class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  #The sentinel business

#This function gets a value from a certain index
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1    #Return this value for an incorrect one
        curr = self.head     
        for _ in range(index + 1):   #The loop to return the value at said index
            curr = curr.next
        return curr.val
    
#This function inserts a value at the head
    def addAtHead(self, val):
        self.addAtIndex(0, val)
#This function inserts a value at the tail
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
#This function inserts a value at a defined index
    def addAtIndex(self, index, val):
        if index > self.size:  #Take care of index values greater than the size of the list
            return "Out of range"
        if index < 0:
            index = 0
        self.size+=1 
        pred = self.head
        for _ in range(index):
            pred = pred.next     
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add
#This function removes a value at a defined index
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:  #When the index is greated than the size of the list
            return "Out of range"
        self.size -=1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next
#This function prints the values of the LinkedList
    def PrintList(self):
      my_list = []
      cur_node = self.head
      while cur_node.next != None:
        cur_node = cur_node.next
        my_list.append(cur_node.val)
      print(my_list)
 
#Play around with the an instance of the class
start_ = MyLinkedList()
start_.PrintList()
start_.addAtHead(8)
start_.PrintList()
start_.addAtTail(6)
start_.PrintList()
start_.addAtIndex(2,7)
start_.PrintList()
start_.addAtTail(8)
start_.PrintList()
