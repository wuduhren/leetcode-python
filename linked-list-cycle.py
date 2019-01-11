#https://leetcode.com/problems/linked-list-cycle/
class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if (fast==slow):
                return True
        return False