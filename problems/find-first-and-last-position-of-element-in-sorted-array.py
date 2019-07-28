"""
First, we search the target by switch pointer `p`.
    * Starting at middle. `p = (l+r)/2`.
    * If the `nums[p]>target`, we do the same search on the left-half of nums.
    * If the `nums[p]<target`, we do the same search on the right-half of nums.
    * Until we find the target.
If the target is not in the `nums` the pointer `p` will stop moving. `return [-1, -1]`.

Second, we move pointers, `l`, `r` to find the right-most and left-most targets.

The time complexity is O(LogN), becuase we use the concept of binary search to find the `target`.
"""
class Solution(object):
    def searchRange(self, nums, target):
        if nums is None or len(nums)==0:
            return [-1, -1]

        l = 0
        r = len(nums)
        p = (l+r)/2

        while nums[p]!=target:
            if nums[p]>target: r = p
            else: l = p

            p_next = (l+r)/2
            if p==p_next: return [-1, -1]
            p = p_next

        l = r = p
        while r+1<len(nums) and nums[r+1]==target:
            r = r+1
        while 0<=l-1 and nums[l-1]==target:
            l = l-1
        return [l, r]
