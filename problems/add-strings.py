class Solution(object):
    def addStrings(self, nums1, nums2):
        ans = ''
        i = len(nums1)-1
        j = len(nums2)-1
        
        carry = 0
        while 0<=i and 0<=j:
            n1 = int(nums1[i])
            n2 = int(nums2[j])
            total = n1+n2+carry
            n = total%10
            carry = 1 if total>=10 else 0
            ans = str(n)+ans
            i -= 1
            j -= 1
        
        while 0<=i:
            total = int(nums1[i])+carry
            n = total%10
            carry = 1 if total>=10 else 0
            ans = str(n)+ans
            i -= 1
        
        while 0<=j:
            total = int(nums2[j])+carry
            n = total%10
            carry = 1 if total>=10 else 0
            ans = str(n)+ans
            j -= 1
        
        if carry: ans = str(carry)+ans
        
        return ans