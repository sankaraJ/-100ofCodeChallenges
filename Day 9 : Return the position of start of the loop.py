#Parts of the code adopted from 
# https://leetcode.com/problems/linked-list-cycle-ii/

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pt1 = pt2 = head
        flag = False

        while pt2 and pt2.next:
            pt1 = pt1.next
            fast = pt2.next.next

            if pt1 == pt2:
                flag = True
                break

        if flag:
            pt1 = head
            while pt1 != pt2:
                pt1 = pt1.next
                pt2 = pt2.next

            return pt1

        return None
