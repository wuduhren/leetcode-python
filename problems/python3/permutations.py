"""
Time: O(N!), since we call helper() N! times.
Space: O(N) for recursion stacks.

Whenever we call `helper()`, we pick a num that is not "used" and add it to the `permutation`.
Recursively call the `helper()` until we filled the `permutation`.
Resotre `permutation` and `used` and try another `num`.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper():
            if len(permutation)==len(nums):
                ans.append(permutation.copy())
                return
            
            for num in nums:
                if num in used: continue
                used.add(num)
                permutation.append(num)
                helper()
                used.remove(num)
                permutation.pop()
        
        ans = []
        permutation = []
        used = set()
        helper()
        return ans