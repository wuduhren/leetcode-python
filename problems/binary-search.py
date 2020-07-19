"""
First, see if target is larger then the largest or smaller then the smallest
If it is out of range, it is not in the `nums`.

Second, we use two pointers `l`, `r` to navigate our *binary search*.
For every iteration, we choose the index, middle between `l` and `r` as `p`.
If the value at `p` is larger than the target, we search the left-half by `r = p-1`.
If the value at `p` is smaller than the target, we search the right-half by `l = p+1`.
Continue this proccess, until we find the value.

If we can't find the value, then `l` and `r` are going to collapse. `return -1`

Another solution is to use [bisect](https://docs.python.org/2.7/library/bisect.html).
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

import bisect
class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums)==0: return -1
        if target<nums[0] or nums[-1]<target: return -1 #check if out of range

        i = bisect.bisect_left(nums, target)

        #check if target in `nums`
        if nums[i]==target: return i
        else: return -1


# 2020/7/19
class Solution(object):
    def search(self, nums, target):
        if not nums: return -1

        l = 0
        r = len(nums)-1

        while True:
            if l>r: break
            if target<nums[l]: return -1
            if nums[r]<target: return -1

            if target==nums[l]: return l
            if target==nums[r]: return r

            m = (l+r)/2
            if target==nums[m]:
                return m
            elif target<nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
