class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        head = nums[0]
        slow = head
        fast = head
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast: break
        
        slow = head
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow