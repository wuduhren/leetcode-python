"""
j is the index to insert when a number not equal to val.
j will never catch up i, so j will not mess up the check.
"""
class Solution(object):
    def removeElement(self, nums, val):
        j = 0
        for n in nums:
            if n!=val:
                nums[j] = n
                j += 1
        return j