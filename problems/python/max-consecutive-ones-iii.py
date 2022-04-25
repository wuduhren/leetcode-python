class Solution(object):
    def longestOnes(self, nums, k):
        ans = 0
        zeroCount = 0
        i = 0
        
        for j, num in enumerate(nums):
            if num==0: zeroCount += 1
            
            while zeroCount>k:
                if nums[i]==0: zeroCount -= 1
                i += 1
            ans = max(ans, j-i+1)
        
        return ans