"""
This answer is the python version of the offical answer.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def nextPermutation(self, nums):
        def reverse(start):
            end = len(nums)-1
            
            while start<end:
                swap(start, end)
                start += 1
                end -= 1
        
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        
        i = len(nums)-2
        
        while i>=0 and nums[i+1]<=nums[i]:
            i -= 1
        
        if i>=0:
            j = len(nums)-1
            while nums[j]<=nums[i]: j -= 1
            swap(i, j)
        
        reverse(i+1)
        return nums