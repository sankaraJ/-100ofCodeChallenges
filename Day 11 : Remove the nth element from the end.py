#Inspired by 
## https://leetcode.com/problems/remove-nth-node-from-end-of-list/
### Parts of the code adopted from 
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/1196549/python-solution

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        
        my_list = ListNode(next = head)
        l = 0
        pos_n = head
        while pos_n:
            pos_n = pos_n.next
            l = l + 1
        count = l - n
        pos_n = my_list
        
        while count != 0:
            pos_n = pos_n.next
            count = count - 1
        
        pos_n.next = pos_n.next.next
        return my_list.next 
