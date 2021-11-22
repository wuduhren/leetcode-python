"""
`nums = [1, 2, 3, 4, 5]`
The first time you choose you can either choose 1 or 2 or 3 or 4 or 5. Lets say you choose 2. So the path so far is `[2]`.
The second time you choose you can only choose 1 or 3 or 4 or 5. Lets say you choose 3. So the path so far is `[2, 3]`.
The third time you choose you can only choose 1 or 4 or 5. Lets say you choose 1. So the path so far is `[2, 3, 1]`.
The third time you choose you can only choose 4 or 5...
.
.
.

We put the numbers we can choose in the `options` parameter. And the path so far in the `path` parameter.
In each `dfs()` we check if the path has used up all the numbers in the `nums`. If true. Append it in the output.
If not, we explore all the posible path in the `options` by `dfs()`.

The time complexity is O(N!). Since in this example our choices is 5 at the beginning, then 4, then 3, then 2, then 1.
The space complexity is O(N!), too. And the recursion takes N level of recursion.
"""
class Solution(object):
    def permute(self, nums):
        def dfs(path, options):
            if len(nums)==len(path):
                opt.append(path)
                return
            for i, nums in enumerate(options):
                dfs(path+[nums], options[:i]+options[i+1:])

        opt = []
        dfs([], nums)
        return opt




"""
Time complexity: O(N!). Since in this example our choices is N at the beginning, then N-1, then N-2, then N-3... then 1.
Space complexity: O(N!). The recursion takes N level of recursion.

For each `dfs()` we put the `n` in `remains` to the `path`, if there is no `remains`, add the `path` to the `ans`.
"""
class Solution(object):
    def permute(self, nums):
        def dfs(remains, path):
            if not remains: ans.append(path)
            
            for i, n in enumerate(remains):
                dfs(remains[:i]+remains[i+1:], path+[n])
        
        ans = []
        dfs(nums, [])
        return ans


"""
Time: O(N!)
Space: O(N!)

helper(0) will set index 0 to all number.
helper(1) will set index 1 to all number remains.
helper(2) will set index 2 to all number remains.
helper(3) will set index 3 to all number remains.
...
"""
class Solution(object):
    def permute(self, nums):
        def helper(i):
            if i>=N: ans.append(nums[:])
            
            for j in xrange(i, N):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        
        N = len(nums)
        ans = []
        helper(0)
        return ans