"""
^ (XOR)
The same will be 0
0^0 = 0
1^1 = 0

Different will be 1
1^0 = 1
0^1 = 1
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for num in nums: ans ^= num
        return ans