class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        
        slow = head
        fast = head
        
        while fast:
            slow = slow.next
            
            if not fast.next: return False
            fast = fast.next.next
            
            if slow==fast: return True
        
        return False