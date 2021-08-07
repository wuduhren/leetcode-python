"""
Time: O(N), the while loop will only be executed if `n` is the beginning of a consecutive sequence. So each n will only be iterated once.
Space: O(N).

For each `n` in the set, check if it is a beginning of a consecutive sequence. (`n-1 not in s`)
If so, get the length of the consecutive sequence (`c`) and update the `ans`.
"""
class Solution(object):
    def longestConsecutive(self, nums):
        s = set(nums)
        ans = 0
        
        for n in s:
            if n-1 not in s:
                c = 1
                curr = n
                
                while curr+1 in s:
                    curr = curr+1
                    c += 1

                ans = max(ans, c)
                
        return ans