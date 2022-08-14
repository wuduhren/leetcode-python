#Two pass.
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #count the length of the linked list
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        

        node = head
        steps = count-n-1
        
        #steps==-1 means that we need to remove the first node
        if steps==-1: return head.next
        
        #traverse to the node before the node we wanted to remove
        while steps>0:
            node = node.next
            steps -= 1
        
        #remove "node.next"
        node.next = node.next.next
        
        return head


#One pass. Fast pointer is ahead of slow pointer by n+1
#So slow pointer will stop at the node before the node we wanted to remove
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        ahead = n+1
        fast = dummy
        slow = dummy
        
        while fast:
            fast = fast.next
            ahead -= 1
            if ahead<0: slow = slow.next
        
        slow.next = slow.next.next

        return dummy.next