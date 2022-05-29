class Solution(object):
    def majorityElement(self, nums):
        ans = []
        counter = {}
        requiredCount = len(nums)/3.0
        
        for n in nums:
            if n not in counter: counter[n] = 0
            counter[n] += 1
        
        for n in counter:
            if counter[n]>requiredCount: ans.append(n)
        
        return ans