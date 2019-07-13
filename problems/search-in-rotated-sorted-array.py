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
