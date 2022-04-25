"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        
        for num in nums:
            if num in seen: return True
            seen.add(num)

        return False