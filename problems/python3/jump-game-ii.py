"""
l and r is the index range we can reach within "steps".
So while r can not reach the end (`r<len(nums)-1`), we keep update l, r and steps.

Time: O(N)
Space: O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = 0
        steps = 0
        
        while r<len(nums)-1:
            farest = float('-inf')
            for i in range(l, r+1):
                farest = max(farest, i+nums[i])
            
            l = r+1
            r = farest
            steps += 1
            
        return steps