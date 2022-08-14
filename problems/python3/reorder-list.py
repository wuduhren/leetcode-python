class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle point
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next

        #reverse the linked list after the middle point
        middle = self.reverseList(middle)

        #separate the linked list before the middle
        slow.next = None
        
        #merge two linked list
        node = head
        while middle and node:
            nextNode = node.next
            node.next = middle
            middle = middle.next
            node.next.next = nextNode
            node = nextNode
        return head
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        node = head
        
        while node:
            nextNode = node.next
            node.next = pre
            if not nextNode: return node
            pre = node
            node = nextNode
        