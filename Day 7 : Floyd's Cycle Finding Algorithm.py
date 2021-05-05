#Day : 7   -- Floyd's Cycle Finding Algorithm

class isItCircular_:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:    #A ciclical list is determined by the head. A good place to start with
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:   #The faster one will already be in the list
                return False
            slow = slow.next
            fast = fast.next.next
        return True
