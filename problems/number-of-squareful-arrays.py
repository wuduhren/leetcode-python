"""
Time: O(N!)
Space: O(N!)

Create a helper function:
If there is no remains, ans += 1
Check the last num in the permutaion, last
For each num in remains see if it and the last sum to a square number
If true, call helper

Also, if the number is the same as the previous one, skip it, since we already explore the number.
"""

class Solution(object):
    def __init__(self):
        self.ans = 0
        
    def numSquarefulPerms(self, nums):
        def isSquare(num):
            return int(math.sqrt(num))**2==num
        
        def helper(per, remains):
            if not remains: self.ans += 1
            last = per[-1]
            
            for i, n in enumerate(remains):
                if i>0 and n==remains[i-1]: continue
                if isSquare(last+n):
                    helper(per+[n], remains[:i]+remains[i+1:])
        
        nums.sort()
        for i, n in enumerate(nums):
            if i>0 and n==nums[i-1]: continue
            helper([nums[i]], nums[:i]+nums[i+1:])
        
        return self.ans