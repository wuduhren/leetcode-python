"""
Time: O(N)
Space: O(1)

Calculate the prefix sum. Whenever the prefix is negative, we ignore all the value before.
Update the ans along the way.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        currSum = 0
        
        for num in nums:
            if currSum<0: currSum = 0
            currSum += num
            ans = max(ans, currSum)
        return ans