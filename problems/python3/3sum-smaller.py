class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = 0
        
        nums.sort()
        
        
        for i in range(N):
            j = i+1
            k = N-1
            while j<k:
                if nums[i]+nums[j]+nums[k]<target:
                    ans += k-j
                    j += 1
                else:
                    k -= 1
        return ans