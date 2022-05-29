"""
Time: O(N)
Space: O(1)

Floyd's Tortoise and Hare Algorithm: Given a linked list, return the node where the cycle begins.
"""
class Solution(object):
    def findDuplicate(self, nums):

        #find the intersect node, where slow and fast pointer meets.
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast: break
        
        #find the intersect node, where slow and slow2 pointer meets. slow2 is starting from the begin.
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow==slow2: return slow
        
        return 0