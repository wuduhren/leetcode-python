class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        #number of subarrays with sum at most "goal"
        def atMost(goal):
            ans = 0
            total = 0
            i = 0
            
            for j, num in enumerate(nums):
                if num==1: total += 1
                
                while i<len(nums) and total>goal:
                    if nums[i]==1: total -= 1
                    i += 1
                
                ans += j-i+1 #number of subarrays that can generate from nums[i~j]
            return ans
        
        return atMost(goal)-atMost(goal-1) if goal>0 else atMost(goal)