#Recursive
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        temp = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return temp

#Iterative
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        node = head
        
        while node:
            nextNode = node.next
            node.next = pre
            if not nextNode: return node
            pre = node
            node = nextNode