"""
dfs(l, r) return the max coins that we can get at range l to r.

```
for i in range(l, r+1):
    dp[(l, r)] = max(dp[(l, r)], nums[l-1]*nums[i]*nums[r+1] + dfs(l, i-1) + dfs(i+1, r))
```
Assuming i is the last one we extract, the max coins we can get.

Start from the last becasue, we are not able to track the neighbor if we start from the first we extract.

Time: O(N^3)
Space: O(N^2)
"""
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(l, r)->int:
            if l>r: return 0
            if (l, r) in dp: return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r+1):
                dp[(l, r)] = max(dp[(l, r)], nums[l-1]*nums[i]*nums[r+1] + dfs(l, i-1) + dfs(i+1, r))
            return dp[(l, r)]
                
        nums = [1]+nums+[1]
        dp = {}
        return dfs(1, len(nums)-2)