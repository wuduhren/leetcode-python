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

"""
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""