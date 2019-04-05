#https://leetcode.com/problems/reverse-linked-list/
class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            
        return prev

