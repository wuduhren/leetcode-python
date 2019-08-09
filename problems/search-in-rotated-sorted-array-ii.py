"""
We use binary search if the interval is sorted (`nums[l]<nums[r]`).
If it is not sorted, we cut the array into half, to see
    * If the left half is sorted and the target is in the range. If so, look into the left part. (`r = p-1`)
    * If the right half is sorted and the target is in the range. If so, look into the right part. (`l = p+1`)
    * Else we can only move the `r` and `l` to the middle. (`r = r-1`, `l = l+1`). For example, `[1,1,1,1,1,1,1,3,1,1,1]`.
The time complexity sits between, `O(LogN)` and `O(N)`.
If there are a lots of the same value, we like `[1,1,1,1,1,1,1,3,1,1,1]` the time will closer to O(N). Vise versa.
"""
class Solution(object):
    def search(self, nums, t):
        if nums is None or len(nums)==0: return False
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            if nums[l]==t or nums[p]==t or nums[r]==t:
                return True

            if nums[l]<nums[r]:
                #check if out of ragne
                if t<nums[l] or nums[r]<t: return False
                #binary search
                if t<nums[p]:
                    r = p-1
                else:
                    l = p+1
            else:
                if nums[l]<nums[p] and nums[l]<t and t<nums[p]:
                    r = p-1
                elif nums[p]<nums[r] and nums[p]<t and t<nums[r]:
                    l = p+1
                else:
                    r = r-1
                    l = l+1
        return False
