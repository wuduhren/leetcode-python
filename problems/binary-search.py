"""
First, see if target is larger then the largest or smaller then the smallest
If it is out of range, it is not in the `nums`.

Second, we use two pointers `l`, `r` to navigate our *binary search*.
For every iteration, we choose the index, middle between `l` and `r` as `p`.
If the value at `p` is larger than the target, we search the left-half by `r = p-1`.
If the value at `p` is smaller than the target, we search the right-half by `l = p+1`.
Continue this proccess, until we find the value.

If we can't find the value, then `l` and `r` are going to collapse. `return -1`
"""
class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums)==0: return -1
        if target<nums[0] or nums[-1]<target: return -1 #test is out of range
        l = 0
        r = len(nums)-1

        while r>=l:
            if nums[l]==target: return l
            if nums[r]==target: return r
            p = (l+r)/2
            if nums[p]==target:
                return p
            elif nums[p]>target:
                r = p-1
            else:
                l = p+1
        return -1
