"""
We use binary search if the interval is sorted (`nums[l]<nums[r]`).
If it is not sorted, we cut the array into half, to see
    * If the left half is sorted and the target is in the range. If so, look into the left part. (`r = p-1`)
    * If the right half is sorted and the target is in the range. If so, look into the right part. (`l = p+1`)
    * Else we can only move the `r` and `l` to the middle. (`r = r-1`, `l = l+1`). For example, `[1,1,1,1,1,1,1,3,1,1,1]`.
The time complexity sits between, `O(LogN)` and `O(N)`.
If there are a lots of the same value, we like `[1,1,1,1,1,1,1,3,1,1,1]` the time will closer to O(N). Vise versa.
"""
class Solution(object):
    def search(self, nums, t):
        if nums is None or len(nums)==0: return False
        l = 0
        r = len(nums)-1

        while l<=r:
            p = (l+r)/2
            if nums[l]==t or nums[p]==t or nums[r]==t:
                return True

            if nums[l]<nums[r]:
                #check if out of ragne
                if t<nums[l] or nums[r]<t: return False
                #binary search
                if t<nums[p]:
                    r = p-1
                else:
                    l = p+1
            else:
                if nums[l]<nums[p] and nums[l]<t and t<nums[p]:
                    r = p-1
                elif nums[p]<nums[r] and nums[p]<t and t<nums[r]:
                    l = p+1
                else:
                    r = r-1
                    l = l+1
        return False


#2020/7/20, recursive.
class Solution(object):
    def search(self, nums, target):
        def binary_search(l, r):
            if l>r: return False
            if nums[l]==target: return True
            if nums[r]==target: return True

            m = (l+r)/2
            if nums[m]==target:
                return m
            if target<nums[m]:
                return binary_search(l, m-1)
            else:
                return binary_search(m+1, r)
        
            if not nums: return False
        
        def helper(l, r):
            if l>r: return False
            if nums[l]==target: return True
            if nums[r]==target: return True
            if nums[l]<nums[r]: return binary_search(l+1, r-1)
            
            m = (l+r)/2
            if nums[m]==target: return m

            if helper(l+1, m-1): return True
            if helper(m+1, r-1): return True
            return False
        
        if not nums: return False
        return helper(0, len(nums)-1)


"""
Time: O(LogN). Worse Case: O(N).
Space: O(1)

The key idea for most rotated array question is that
If you cut a rotated array into half,
One half will be in-order.
One half will be rotated or in-order.
"""
class Solution(object):
    def search(self, A, T):
        N = len(A)
        l = 0
        r = N-1
        
        while l<=r:

            #skip repeated numbers
            while r>0 and A[r]==A[r-1]: r -= 1
            while l<N-1 and A[l]==A[l+1]: l += 1
            while r>0 and A[l]==A[r]: r -= 1
            while l<N-1 and A[l]==A[r]: l += 1
            
            m = (l+r)/2
            
            if A[l]==T or A[m]==T or A[r]==T: return True
            
            if A[l]<=A[m] and A[m]<=A[r]:
                #l~r is in-order, standard binary search.
                if T<A[l] or T>A[r]: return False #out of range l~r
                
                if A[m]<T:
                    l = m+1
                else:
                    r = m-1
            elif A[l]<=A[m]:
                #l~m is in-order

                if A[l]<T and T<A[m]:
                    #T is in l~m, so search in l~m
                    r = m-1
                else:
                    #T is not in l~m, so search in m~r
                    l = m+1
            else:
                #m~r is in-order

                if A[m]<T and T<A[r]:
                    #T is in m~r, so search m~r
                    l = m+1
                else:
                    #T is not in m~r, so search in l~m
                    r = m-1
        
        return False
        