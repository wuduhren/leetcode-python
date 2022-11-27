"""
Time: O(NS), S is sum(nums), N is len(nums). This is the max possible number of element in "history". Which will be lesser than 2^N.
Space: O(NS)
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr):
            #cache
            if (i, curr) in history:
                return history[(i, curr)]
            
            #ending condition
            if i==len(nums):
                if curr==target:
                    history[(i, curr)] = 1
                else:
                    history[(i, curr)] = 0
                return history[(i, curr)]
            
            history[(i, curr)] = dfs(i+1, curr+nums[i])+dfs(i+1, curr-nums[i])
            return history[(i, curr)]
        
        ans = 0
        history = {}
        return dfs(0, 0)