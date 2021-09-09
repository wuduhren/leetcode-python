"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def missingNumber(self, nums):
        maxNum = max(nums)
        s = set(nums)
        
        for num in xrange(maxNum+1):
            if num not in s:
                return num
        
        return maxNum+1

"""
Time: O(N)
Space: O(1)

[0] Gauss' Formula: 0+1+2+...+n = n*(n+1)/2
[1] Knowing that there is a missing num in nums, the last/max num will be len(nums).
"""
class Solution:
    def missingNumber(self, nums):
        n = len(nums) #[1]
        expectedSum = n*(n+1)/2 #[0]
        actualSum = sum(nums)
        return expectedSum-actualSum