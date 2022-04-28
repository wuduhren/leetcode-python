"""
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        N = len(nums)
        ans = float('inf')
        
        for i in range(N):
            j = i+1
            k = N-1
            
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total==target: return total
                if abs(target-ans)>abs(target-total): ans = total
                if total>target:
                    k -= 1
                elif total<target:
                    j += 1
        return ans