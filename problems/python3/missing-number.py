class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        ans = 0
        
        for n in range(N+1):
            ans ^= n
        
        for n in nums:
            ans ^= n
        
        return ans