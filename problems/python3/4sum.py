"""
Time: O(N^(K-1)) -> O(N^3)
Space: O(K) -> O(1)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(k, start, target):
            if k>2:
                for i in range(start, len(nums)-k+1):
                    if i!=start and nums[i]==nums[i-1]: continue
                    temp.append(nums[i])
                    kSum(k-1, i+1, target-nums[i])
                    temp.pop()
            else:
                l, r = start, len(nums)-1
                
                while l<r:
                    if nums[l]+nums[r]>target:
                        r -= 1
                    elif nums[l]+nums[r]<target:
                        l += 1
                    else:
                        ans.append(temp+[nums[l], nums[r]])
                        while l<r and nums[l+1]==nums[l]: l += 1
                        while l<r and nums[r-1]==nums[r]: r -= 1
                        l += 1
                        r -= 1
                        
        ans = []
        temp = []
        nums.sort()
        kSum(4, 0, target)
        return ans