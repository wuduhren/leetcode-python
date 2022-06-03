"""
Time: O(N * 2^N)
Space: O(N)
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i==len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            
            while i+1<len(nums) and nums[i]==nums[i+1]: i += 1
            helper(i+1)
            
        nums.sort()
        ans = []
        subset = []
        helper(0)
        return ans