#https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #Compare nums1 and nums2 from backward
        #Put the larger one to nums1's end
        #If one of the array is done
        #The rest is already sorted
        #Just put them in place
        
        i = m+n-1 #cursor on nums1 that we are editting
        i1 = m-1 #cursor on nums1
        i2 = n-1 #cursor on nums2
        
        while i1>=0 and i2>=0:
            if nums1[i1]>nums2[i2]:
                nums1[i] = nums1[i1]
                i1 = i1-1
                i = i-1
            else:
                nums1[i] = nums2[i2]
                i2 = i2-1
                i = i-1
        
        #One of the array is done, put the rest in place
        nums1[:i2+1] = nums2[:i2+1]