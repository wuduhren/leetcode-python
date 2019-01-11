#https://leetcode.com/problems/maximum-subarray/
class Solution(object):
    def maxSubArray(self, nums):
        maxCurrent = []
        for i in range(0, len(nums)):
            n = nums[i]
            if (i==0):
                maxCurrent.append(n)
            else:
                if (n>n+maxCurrent[i-1]):
                    maxCurrent.append(n)
                else:
                    maxCurrent.append(n+maxCurrent[i-1])
        return max(maxCurrent)