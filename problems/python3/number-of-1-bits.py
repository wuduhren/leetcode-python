"""
n = n&(n-1) will turn the right most 1 to 0.
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n>0:
            n = n&(n-1)
            ans += 1
        return ans