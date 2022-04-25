"""
For each iteration, if we found a new starting point we will append previous range to the opt.
The range start from index s to index i-1.
"""
class Solution(object):
    def summaryRanges(self, nums):
        nums.append('#')
        opt = []
        s = 0
        
        for i in xrange(1, len(nums)):
            if nums[i-1]+1!=nums[i]:
                if i-1>s:
                    opt.append(str(nums[s])+'->'+str(nums[i-1]))
                else:
                    opt.append(str(nums[s]))
                s = i
        return opt