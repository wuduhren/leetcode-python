class Solution(object):
    def firstMissingPositive(self, nums):
        N = len(nums)
        
        if 1 not in nums: return 1
        
        for i, num in enumerate(nums):
            if num<=0 or num>N:
                nums[i] = 1
        
        for i in xrange(N):
            a = abs(nums[i])
            
            if a==N:
                nums[0] = -abs(nums[0])
            else:
                nums[a] = -abs(nums[a])
        
        for i in xrange(1, N):
            if nums[i]>0: return i
        if nums[0]>0: return N
        
        return N+1

"""
Time: O(N), each num is going to be swap once.
Space: O(1).

For nums with length N, the answer must be in between 1~N+1.

[1] So for number between 1~N, lets put them in the right place.
number 1 will be stored at index 0.
number 2 will be stored at index 1.
...
number n will be stored at index n-1.


[2] Check if any number are not in place.

[3] If all the number are in place, then the ans must be N+1.
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        N = len(nums)
        
        #[1]
        for i in xrange(N):
            while 1<=nums[i]<=N and nums[i]!=i+1:
                j = nums[i]-1
                if nums[i]==nums[j]: break #otherwise they are going to keep swapping infinitely, because one of them is not inplace.
                nums[i], nums[j] = nums[j], nums[i]
        
        #[2]
        for i in xrange(N):
            if nums[i]!=i+1: return i+1
        
        #[3]
        return N+1