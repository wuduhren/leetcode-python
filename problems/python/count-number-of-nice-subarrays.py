class Solution(object):
    def numberOfSubarrays(self, nums, K):
        def atMost(k):
            oddCount = 0
            ans = 0
            i = 0
            
            for j in xrange(len(nums)):
                if nums[j]%2!=0: oddCount += 1
                
                while oddCount>k:
                    if nums[i]%2!=0: oddCount -= 1
                    i += 1
                
                ans += j-i+1
            
            return ans
        
        return atMost(K)-atMost(K-1)