"""
j is the index to insert when a "new" number are found.
For each iteration, nums[:j] is the output result we currently have.
So nums[i] should check with nums[j-1] and nums[j-2].
"""
class Solution(object):
    def removeDuplicates(self, nums):
        j = 2
        
        for i in xrange(2, len(nums)):
            if not (nums[i]==nums[j-1] and nums[i]==nums[j-2]):
                nums[j] = nums[i]
                j += 1
        return j