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


"""
Time: O(N!)
Space: O(N!)

Since we are iterating the key of the counter, we will only place "each kind of number" at the first place once.
For example, [1,1,2], it will not happend that
We place the first "1" at index 0, and keep exploring...
And place the second "1" at index 0, and keep exploring...
"""
class Solution(object):
    def permuteUnique(self, nums):
        def helper(path):
            if len(path)==len(nums): ans.append(path[:])
            
            for num in counter:
                if counter[num]>0:
                    path.append(num)
                    counter[num] -= 1
                    
                    helper(path)
                    
                    path.pop()
                    counter[num] += 1
        ans = []
        counter = collections.Counter(nums)
        helper([])
        return ans


"""
差板法
"""
class Solution(object):
    def permuteUnique(self, nums):
        if not nums: return []
        
        permutations = collections.deque([[nums[0]]])
        
        for i in xrange(1, len(nums)):
            num = nums[i]
            l = len(permutations)    
            
            while l:
                permutation = permutations.popleft()
                for j in xrange(len(permutation)+1):
                    if 0<j and num==permutation[j-1]: break
                    newPermutaion = permutation[:]
                    newPermutaion.insert(j, num)
                    permutations.append(newPermutaion)
                l -= 1
        
        return permutations