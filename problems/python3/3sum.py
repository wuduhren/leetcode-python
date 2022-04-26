"""
Time: O(N^2)
Space: O(1)

First of all, we need to sort the list, so that it is easier to know where to move the pointers.
(Keep in mind that sorting takes O(NLogN) of time, but since judging from the problem this solution might takes at least O(N^2), so it is ok to sort.)

Now, we have 3 unique pointers at the list. i, j, k, where i<j<k.
For a given i, set j at i+1 and k at the rightest.

If the sum is too large, our only option is to move k left, so we can find smaller sum.
If the sum is too small, our only option is to move j right, so we can find larger sum.
If the sum is what we want, add it to the ans.

[0] we need to skip the num that is the same as the last one to remove duplicate. This is actually the hardest part of the problem.
[1] if nums[i] is larger than 0, we can stop, since nums[i] and nums[k] are surely larger than nums[i]
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i in range(len(nums)):
            if 0<i and nums[i]==nums[i-1]: continue #[0]
            if nums[i]>0: break #[1]
            
            j, k = i+1, len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]>0:
                    k -= 1
                elif nums[i]+nums[j]+nums[k]<0:
                    j += 1
                else:
                    ans.append((nums[i], nums[j], nums[k]))
                    while 0<k-1 and nums[k-1]==nums[k]: k -= 1 #[0]
                    while j+1<len(nums) and nums[j+1]==nums[j]: j += 1 #[0]
                    k -= 1
                    j += 1
                    
        return ans