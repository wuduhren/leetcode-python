class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy
        
        while l1 or l2 or carry:
            n = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if n>=10:
                curr.next = ListNode(n-10)
                carry = 1
            else:
                curr.next = ListNode(n)
                carry = 0
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next