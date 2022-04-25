from bisect import bisect_left

class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1 for _ in nums]
        
        for i in xrange(1, len(nums)):
            for j in xrange(i-1, -1, -1):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
"""
Time: O(N^2)
Spacce: O(N)
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        dp = []

        for n in nums:
            i = bisect_left(dp, n)
            if i==len(dp):
                dp.append(n)
            else:
                dp[i] = n
                
        return len(dp)

"""
dp[i] := the smallest ending number that has length i+1
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        dp = [1]*len(nums)
        
        for i in xrange(1, (len(nums))):
            for j in xrange(i-1, -1, -1):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
"""
dp[i] := longest increasing subsequence that ends at nums[i]
dp[i] = max{ dp[j] where j = 0~i-1 } + 1
"""