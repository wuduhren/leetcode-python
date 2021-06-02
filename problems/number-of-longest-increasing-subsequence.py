class Solution(object):
    def findNumberOfLIS(self, nums):
        L = [1]*len(nums) #LIS
        C = [1]*len(nums)
        
        for i in xrange(len(nums)):
            for j in xrange(i):
                if nums[i]>nums[j]:
                    if L[j]+1==L[i]:
                        # If L[j]+1==L[i], it means that the combination of L[j] can simply append nums[i] and reach L[i]
                        # So add the C[j] to C[i]
                        C[i] += C[j]
                    elif L[j]+1>L[i]:
                        # If L[j]+1==L[i], it means that the combination of L[j] can simply append nums[i] and exceed L[i]
                        # So update L[i] to L[j]+1 and C[i] to C[j]
                        L[i] = L[j]+1
                        C[i] = C[j]
        
        max_length = max(L)
        max_length_count = 0
        for i, count in enumerate(C):
            if L[i]==max_length:
                max_length_count+=count
        return max_length_count

"""
Time: O(N^2)
Spance: O(N)
"""


class Solution(object):
    def findNumberOfLIS(self, nums):
        dp = [1]*len(nums)
        count = [1]*len(nums)
        count[0] = 1
        
        for i in xrange(1, (len(nums))):
            for j in xrange(i-1, -1, -1):
                if nums[i]>nums[j]:
                    if dp[j]+1>dp[i]:
                        count[i] = count[j]
                        dp[i] = dp[j]+1
                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]       
        print count
        
        maxLis = max(dp)
        ans = 0
        for i, lis in enumerate(dp):
            if lis==maxLis: ans += count[i]
        
        return ans
"""
dp[i] := longest increasing subsequence that ends at nums[i]
count[i] := number of comfination that ends up dp[i].

dp[i] = max{ dp[j] where nums[i]>nums[j], j = 0~i-1 } + 1

Time: O(N^2)
Space: O(N)
"""