"""
Time: O(N^2), this will get TLE
Space: O(N)

prefixSum[i] == sum(nums[:i]) (nums[0] + nums[1] + ... + nums[i-1])
prefixSum[j]-prefixSum[i] == sum(nums[i:j]) (nums[i] + nums[i+1] + ... + nums[j-1])
By iterating through all i and j possibilities, we get all the subarray sum that equals to k.
"""
class Solution(object):
    def subarraySum(self, nums, k):
        N = len(nums)
        prefixSum = [0]
        ans = 0
        
        temp = 0
        for n in nums:
            temp += n
            prefixSum.append(temp)
        
        for i in xrange(N+1):
            for j in xrange(i+1, N+1):
                if prefixSum[j]-prefixSum[i]==k: ans += 1
        
        return ans


"""
Time: O(N)
Space: O(N)

Let's optimize from above solution.
Let prefixSum[j] as J.
Let prefixSum[i] as I.

We are basically looking for J-I that equals to k. (J-I == k)
In other words, given a J we are actually looking for an I that eauals to J-k.
If there are, 3 I that equals to J-k exists beforehand, there are 3 J-I combinations that equal to k.
ans += 3
"""
class Solution(object):
    def subarraySum(self, nums, k):
        N = len(nums)
        ans = 0
        
        prefixSumCount = collections.Counter()
        prefixSumCount[0] = 1
        
        J = 0
        for n in nums:
            J += n
            I = J-k #the I that we are looking for.
            ans += prefixSumCount[I] #there are "prefixSumCount[I]" combinations of J-I that equals to k.
            prefixSumCount[J] += 1
            
        return ans