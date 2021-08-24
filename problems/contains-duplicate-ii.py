"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        lastSeen = {}
        
        for i, num in enumerate(nums):
            if num in lastSeen:
                if i-lastSeen[num]<=k: return True
            lastSeen[num] = i
            
        return False