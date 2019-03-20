#https://leetcode.com/problems/two-sum/
"""
I really take time to explain my solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""
class Solution(object):
    def twoSum(self, nums, target):
        for idx, val in enumerate(nums):
            for idx2 in range(idx+1, len(nums)):
                val2 = nums[idx2]
                if ((val+val2)==target):
                    return [idx, idx2]