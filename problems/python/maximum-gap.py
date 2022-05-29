"""
Time: O(N). For radix sort, each digit runs 2 pass on the nums => O(dN).
Since the number of the digit is fixed in range 10 (stated in the problem) => O(dN) ~= O(N).

Space: O(N)
"""
class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2: return 0
        
        self.radixSort(nums)
        
        ans = 0
        for i in xrange(1, len(nums)):
            ans = max(ans, abs(nums[i]-nums[i-1]))
        return ans
    
    def radixSort(self, nums):
        maxNumberOfDigits = len(str(max(nums)))
        
        for d in xrange(maxNumberOfDigits):
            b = [[] for _ in xrange(10)]

            for num in nums:
                n = (num//10**d)%10
                print num, d, n
                b[n].append(num)
            
            i = 0
            for a in b:
                for num in a:
                    nums[i] = num
                    i += 1