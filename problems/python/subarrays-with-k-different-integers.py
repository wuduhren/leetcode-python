class Solution(object):
    def subarraysWithKDistinct(self, nums, K):
        #number of subarray of nums which have at most k different numbers.
        def atMost(k):
            i = 0
            ans = 0
            counter = collections.Counter()
            uniqueCount = 0
            
            for j in xrange(len(nums)):
                counter[nums[j]] += 1
                if counter[nums[j]]==1: uniqueCount += 1
                
                while uniqueCount>k:
                    counter[nums[i]] -= 1
                    if counter[nums[i]]==0: uniqueCount -= 1
                    i += 1
                
                # the logest subarray that ends at j is nums[i:j+1]
                # nums[i:j+1] can produce j-i+1 subarrays that at most has k different number.
                ans += j-i+1
            
            return ans
        
        return atMost(K)-atMost(K-1)