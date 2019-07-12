#https://leetcode.com/problems/reverse-linked-list/
class Solution(object):
    #iterative
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    #recursive
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        new_head = self.reverseList(head.next)
        n = head.next
        n.next = head
        head.next = None
        return new_head
