"""
We use the concept of binary search to find the index.
`l` and `r` indicates the range we are going to search.

First, check if the target is out of range. [0]
Second, check if the target is the same at `l` or `r`. [1]
Third, we use a pivot to navigate our `l` and `r`. [2]
    * If the value on the pivot is larger then the target, we search the left-half.
    * If the value on the pivot is smaller then the target, we search the right-half.
Repeat those three steps.

Last, If we could not find the target, the `l` and `r` will collapse (`l==r`) and it will be the value that is closet to the target. [4]

One thing to keep in mind, if we decided to insert to the right of the index `k`, the output will be `k+1`.
If we decided to insert to the left of the index `k`, the output will be `k`, because we shift all the others to the right.

Time complexity is O(LogN), space complexity is O(1).
"""
class Solution(object):
    def searchInsert(self, nums, target):
        if nums is None or len(nums)==0: return 0
        l = 0
        r = len(nums)-1

        while l<r:
            #[0]
            if nums[l]>target: return l
            if nums[r]<target: return r+1

            #[1]
            if nums[l]==target: return l
            if nums[r]==target: return r

            #[2]
            p = (l+r)/2
            if nums[p]==target:
                return p
            elif nums[p]>target:
                r = p-1
            else:
                l = p+1

        #[4]
        if nums[l]==target:
            return l
        elif nums[l]>target:
            return l
        else:
            return l+1


#2020/7/19
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums: return 0
        
        l = 0
        r = len(nums)-1
        
        while True:
            if l>r: break
            if target<nums[l]: return l
            if target>nums[r]: return r+1
            
            if target==nums[l]: return l
            if target==nums[r]: return r
            
            m = int((l+r)/2)
            
            if target==nums[m]:
                return m
            elif target>nums[m]:
                l = m+1
            else:
                r = m-1
        return 0





