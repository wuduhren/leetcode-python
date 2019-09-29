"""
This is the extended question of the [first one](https://leetcode.com/problems/permutations/submissions/).
The differece is there will be duplicates in the `nums`.

```python
if i>0 and options[i]==options[i-1]: continue
```
Above lets us skip exploring the same path.
We can directly skip the `i` if the value is the same with `i-1`, because `dfs()` on `i-1` has already cover up all the possiblities.

The time complexity is `O(N!)`.
The space complexity is `O(N!)`, too.
"""
class Solution(object):
    def permuteUnique(self, nums):
        def dfs(path, options):
            if len(path)==len(nums):
                opt.append(path)
                return
            for i, n in enumerate(options):
                if i>0 and options[i]==options[i-1]: continue
                dfs(path+[n], options[:i]+options[i+1:])
        opt = []
        nums.sort()
        dfs([], nums)
        return opt
