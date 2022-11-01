"""
Time: O(2^N), 2^0 + 2^1 + 2^2 + 2^3 + ... 2^(N-1) == 2^N-1
Space: O(T), T is the sum of nums
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2!=0: return False
        
        target = total/2
        possibleSum = set()
        possibleSum.add(0)
        for num in nums:
            temp = set()
            for p in possibleSum:
                if p==target or p+num==target: return True
                temp.add(p)
                temp.add(p+num)
            possibleSum = temp
        return False