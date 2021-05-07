#Detecting and removing loops

##Parts of the code adopted from 
#  https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
# Inspired by https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

class Node:
  #Constructor to initialize the node object
  def __init__(self, data):
    self.data = data
    self.next = None

class Linkedlist:
  #Function to initialize the head
  def __init__(self):
    self.head = None

  def detectRemoveLoop(self):
    #pointers on the list
    slow=fast=self.head
    while(slow and fast and fast.next):
      slow = slow.next
      fast = fast.next.next

      #The condition for a loop is when the two pointers meet at some point
      if slow==fast:
        #call a function (defined below) to remove the loop
        self.removeLoop(slow)
        #Return the string for Loop Exists
        return "Loop Exists"
        #Otherwise return loop not found
    return "Loop Not found"

  def removeLoop(self, loop_node):
    ptr1 = self.head
    while (1):
      ptr2 = loop_node
      while (ptr2.next != loop_node and ptr2.next != ptr1):
        ptr2 = ptr2.next
        
      if (ptr2.next == ptr1):
        break
      
      ptr1 = ptr1.next

    ptr2.next = None
#functions to insert nodes and print the list
  def addNode(self, new_node):
    n_ = Node(new_node)
    n_.next = self.head
    self.head = n_

  def printList(self):
    start_ = self.head
    while(start_):
      print(start_.data)
      start_ = start_.next     
