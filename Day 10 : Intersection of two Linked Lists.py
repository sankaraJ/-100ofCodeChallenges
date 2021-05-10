#Insipiration and parts of the code derived from 

### https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        list_a = headA
        list_b = headB
        
        while list_a != list_b:
            list_a = headB if  list_a is None else list_a.next
            list_b = headA if  list_b is None else list_b.next
        return list_a
