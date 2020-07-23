#https://leetcode.com/problems/search-in-rotated-sorted-array/
#we break the nums into two part
#we assume they are sorted
#so in each part, if the target is inside, it will meet
#left_most_number <= target <= right_most_number

#if the target is inside the part
#we do the same calculation to that smaller part

#if we can't find target in both part
#one of two part is not sorted, and the target is inside the not sorted one
#why can we be sure only one part is not sorted?
#because the original array is sorted and just done once rotation
#so we check if it is sorted
#if it is not sorted
#we do the same calculation to that smaller part

#the part will become smaller and smaller exponentially
#so it is O(logN)

class Solution(object):
    def search(self, nums, target):
        if not nums or len(nums)==0:
            return -1

        l = 0
        r = len(nums)-1
        while True:
            m = (l+r)/2

            left_num = nums[l]
            right_num = nums[r]
            mid_num = nums[m]

            if left_num==target:
                return l
            if right_num==target:
                return r
            if mid_num==target:
                return m

            #break the array into two part
            #l~m and m~r

            if left_num<target and target<mid_num:
                #l~m is sorted and target is inside
                #do the same calculation to this part
                r = m-1
                continue

            if mid_num<target and target<right_num:
                #m~r is sorted and target is inside
                #do the same calculation to this part
                l = m+1
                continue

            #if the code goes here
            #the target doesn't exist or
            #one of two part is not sorted
            #the target is in the not sorted part

            if mid_num>right_num:
                #m~r is not sorted
                #check m+1~r
                l = m+1
                continue

            if mid_num<left_num:
                #l~m is not sorted
                #check l~m-1
                r = m-1
                continue

            return -1


"""
If we slice (anywhere) in the rotated-sorted-array, there must be one part already sorted, another part still rotated.
If the right most elemant in the array is greater than the left most (`nums[l]<nums[r]`), then it is **sorted**.
If the array is sorted, we can apply binary search in it.

So for every part of the array, we first determine if it is sorted.
If it is sorted apply binary search.
If it is not sorted, check if the target in the sorted part. If not, search the other part.
"""
class Solution(object):
    def search(self, nums, target):
        if nums is None or len(nums)==0: return -1

        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2

            if nums[l]==target: return l
            if nums[p]==target: return p
            if nums[r]==target: return r

            #array sorted
            if nums[l]<nums[r]:
                #binary search

                #check target is in range
                if target<nums[l] or nums[r]<target:
                    return -1

                if target<nums[p]:
                    r = p-1
                else:
                    l = p+1

            #array not sorted
            else:
                #the left half is sorted
                if nums[l]<nums[p]:
                    #the left half is sorted and target in it, search left.
                    if nums[l]<target and target<nums[p]:
                        r = p-1
                    else:
                        l = p+1

                #the right half is sorted
                else:
                    #the right half is sorted and target in it, search right.
                    if nums[p]<target and target<nums[r]:
                        l = p+1
                    else:
                        r = p-1
        return -1






#2020/7/20, recursive.
class Solution(object):
    def search(self, nums, target):
        def binary_search(l, r):
            if l>r: return -1
            if nums[l]==target: return l
            if nums[r]==target: return r

            m = (l+r)/2
            if nums[m]==target:
                return m
            if target<nums[m]:
                return binary_search(l, m-1)
            else:
                return binary_search(m+1, r)

        if not nums: return -1

        def helper(l, r):
            if l>r: return -1
            if nums[l]==target: return l
            if nums[r]==target: return r
            if nums[l]<=nums[r]: return binary_search(l+1, r-1)
            
            m = (l+r)/2
            if nums[m]==target: return m

            if nums[l]<nums[m]:
                if nums[l]<target and target<nums[m]:
                    return binary_search(l+1, m-1)
                else:
                    return helper(m+1, r)
            else:
                if nums[m]<target and target<nums[r]:
                    return binary_search(m+1, r-1)
                else:
                    return helper(l, m-1)
        
        if not nums: return -1
        return helper(0, len(nums)-1)