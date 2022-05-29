#https://leetcode.com/problems/intersection-of-two-arrays/
class Solution(object):
    #put nums1 to d1'keys, so even if it is repeated, it won't matter
    #if nums2 is d1's keys, put it to nums2'keys
    #the point of using keys to store numbers is to avoid repetition
    def intersection(self, nums1, nums2):
        d1 = {}
        d2 = {}
        for n1 in nums1:
            d1[n1] = 0
        
        for n2 in nums2:
            if n2 in d1:
                d2[n2] = 0
        
        return d2.keys()
    
    #a more elegant way to solve this is to use SET
    #element in set is not repeated
    #set has some convenient build-in operator
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        return nums1.intersection(nums2)