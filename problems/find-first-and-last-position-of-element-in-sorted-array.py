"""
First, we search the target by switch pointer `p`.
    * Starting at middle. `p = (l+r)/2`.
    * If the `nums[p]>target`, we do the same search on the left-half of nums.
    * If the `nums[p]<target`, we do the same search on the right-half of nums.
    * Until we find the target.
If the target is not in the `nums` the pointer `p` will stop moving. `return [-1, -1]`.

Second, we move pointers, `l`, `r` to find the right-most and left-most targets.

The time complexity is O(LogN), becuase we use the concept of binary search to find the `target`.

Another solution is to use [bisect](https://docs.python.org/2.7/library/bisect.html).
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


import bisect
class Solution(object):
    def searchRange(self, nums, target):
        if nums is None or len(nums)==0: return [-1, -1]
        if target<nums[0] or nums[-1]<target: return [-1, -1] #check if target out of range
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)

        if nums[l]!=target or nums[r-1]!=target: return [-1, -1] #check if target in `nums`
        return [l, r-1]


#2020/7/19
class Solution(object):
    def searchRange(self, nums, target):
        def find_range(i, nums):
            start = end = i
            while 0<=start-1 and nums[start-1]==nums[i]:
                start -= 1
            while end+1<len(nums) and nums[end+1]==nums[i]:
                end += 1
            return [start, end]
            
        
        if not nums: return [-1, -1]
        l = 0
        r = len(nums)-1

        while True:
            if l>r: break
            if target<nums[l]: return [-1, -1]
            if target>nums[r]: return [-1, -1]

            if target==nums[l]: return find_range(l, nums)
            if target==nums[r]: return find_range(r, nums)

            m = (l+r)/2
            if target==nums[m]:
                return find_range(m, nums)
            elif target<nums[m]:
                r = m-1
            else:
                l = m+1
        
        return [-1, -1]








