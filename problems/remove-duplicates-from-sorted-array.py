"""
j is the index to insert when a new number are found.
j will never catch up i, so j will not mess up the check.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        for i in xrange(1, len(nums)):
            if nums[i]!=nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j