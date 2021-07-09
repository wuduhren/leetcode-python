"""
Time: O(NLogN)
Space: O(1)
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        i = j = 0
        ans = []
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                ans.append(nums1[i])
                i += 1
                j +=1
            elif nums1[i]>nums2[j]:
                j += 1
            else:
                i += 1
        return ans

"""
Time: O(N)
Space: O(N)
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        c = {} #nums1 counter
        ans = []
        
        for n in nums1:
            if n in c:
                c[n] += 1
            else:
                c[n] = 1
        
        for n in nums2:
            if n in c and c[n]>0:
                ans.append(n)
                c[n] -= 1
        return ans