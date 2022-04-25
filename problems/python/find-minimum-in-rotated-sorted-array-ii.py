"""
If you have not see the [explaination](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/356286/Best-Python-Solution-(How-to-Solve-all-Similar-Problem-Explained)) of the previous [question](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/), please see it first.
This problem has duplicate value in compare to the previous.
The difference is that when you cut the rotated array into half, there might not be a sorted array occur.
You might have something like `[2,2,2,2,1,2,2,2,2,2,2]`.
If we can't find either left-half or right-half is sorted, we simply reduce the range (`l = l+1, r = r-1`) and use the same method again.
"""
class Solution(object):
    def findMin(self, nums):
        if nums is None or len(nums)==0:
            return None
        m = nums[0]
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            m = min(m, nums[l], nums[p], nums[r])

            if nums[l]<nums[r]:
                break
            elif nums[l]<nums[p]:
                l = p+1
            elif nums[p]<nums[r]:
                r = p-1
            else:
                l = l+1
                r = r-1
        return m


"""
Time: O(LogN). Worse Case: O(N).
Space: O(1)

The key idea for most rotated array question is that
If you cut a rotated array into half,
One of the half will be rotated and one half will be in-order. The smallest one must be in the rotated one.
"""
class Solution(object):
    def findMin(self, A):
        N = len(A)
        l = 0
        r = N-1
        
        while l<r:
            #skip the same
            while l<N-1 and A[l]==A[l+1]: l += 1
            while 0<r and A[r]==A[r-1]: r -= 1
            while l<N-1 and A[l]==A[r]: l += 1
            while 0<r and A[l]==A[r]: r -= 1
                
            m = (l+r)/2
            
            if A[l]<=A[m] and A[m]<=A[r]:
                #l~r is in-order, A[l] is the smallest.
                return A[l]
            elif A[l]<=A[m]:
                #l~m is in-order, m~r is rotated. smallet must be in m~r
                l = m+1
            else:
                #m~r is in-order, l~m is rotated. smallet must be in l~m
                r = m
        return A[l]