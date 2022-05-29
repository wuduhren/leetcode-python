"""
Time: O(N)
Space: O(k)
"""
class Solution(object):
    def rotate(self, nums, k):
        if len(nums)<=1: return nums
        
        N = len(nums)
        k = k%N
        store = nums[:k]
        
        for i in xrange(N-1, k-1, -1):
            j = i+k if i+k<N else i+k-N
            nums[j] = nums[i]
        
        for i in xrange(len(store)):
            j = i+k if i+k<N else i+k-N
            nums[j] = store[i]

"""
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def rotate(self, nums, k):
        def reverse(A, start, end):
            while start<end:
                A[start], A[end] = A[end], A[start]
                start += 1
                end -= 1
        

        N = len(nums)
        k = k%N
        reverse(nums, 0, N-1-k)
        reverse(nums, N-k, N-1)
        reverse(nums, 0, N-1)