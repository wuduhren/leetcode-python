"""
Usually the binary search problem, the hard part is to clear all the edge cases.
What will be the edge case? It will be when the recursive function executed at the deepest level. Usually the list with only one or two element.
So I will suggest before submit, try out the case like [0,1] or [1,0] to make sure it will not run unstop.
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def helper(l, r):
            nonlocal ans
            if l>r: return
            
            m = l + int((r-l)/2)
            if nums[l]<=nums[m]:
                ans = min(ans, nums[l])
                helper(m+1, r)
            else:
                ans = min(ans, nums[m+1])
                helper(l, m)
        
        ans = float('inf')
        helper(0, len(nums)-1)
        return ans