"""
Time: O(N * 2^N)
Space: O(N) for "subset".
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if not i<len(nums):
                ans.append(subset.copy())
                return
            
            subset.append(nums[i])
            helper(i+1)
            
            subset.pop()
            helper(i+1)
        
        ans = []
        subset = []
        
        helper(0)
        return ans