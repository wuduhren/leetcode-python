#https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        for idx, val in enumerate(nums):
            for idx2 in range(idx+1, len(nums)):
                val2 = nums[idx2]
                if ((val+val2)==target):
                    return [idx, idx2]