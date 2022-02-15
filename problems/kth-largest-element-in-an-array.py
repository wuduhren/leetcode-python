"""
Sort
Time: O(NLogN)
Space: O(1)
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]

"""
Heap
Time: O(N+KLogN)
Space: O(N)

Python heapq is implemented as a min heap.
"Find Kth Largest" is equal to "Find [len(nums)-(k-1)]th Smallest"
First, heapify the nums, taking O(N)
Second, keep popping the smallest element for len(nums)-(k-1) times. Each taking O(LogN).
"""
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        ans = 0
        k = len(nums)-(k-1)
        heapq.heapify(nums)
        
        while k>0:
            ans = heapq.heappop(nums)
            k -= 1
        
        return ans

"""
Quick Search

Time: O(N) in average case, O(N^2) in worst case.
Spcae: O(1)
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        def sortRange(A, l, r):
            if l>=r: return A

            p = A[(l+r)/2]
            i = partition(A, l, r, p)
            if k<i:
                sortRange(A, l, i-1)
            else:
                sortRange(A, i, r)
            return A

        def partition(A, l, r, p):
            while l<=r:
                while A[l]<p: l += 1
                while A[r]>p: r -= 1
                if l<=r:
                    A[l], A[r] = A[r], A[l]
                    l += 1
                    r -= 1
            return l
        
        k = len(nums)-k #redefine the problem to find the kth nums when sorted
        sortRange(nums, 0, len(nums)-1)
        return nums[k]


#Quick Select
class Solution(object):
    def findKthLargest(self, nums, K):
        def quickSelect(A, s, e, K):
            pivot = A[(s+e)/2]
            i = s
            t = s
            j = e
            
            while t<=j:
                if A[t]<pivot:
                    A[i], A[t] = A[t], A[i]
                    i += 1
                    t += 1
                elif A[t]==pivot:
                    t += 1
                else:
                    A[t], A[j] = A[j], A[t]
                    j -= 1
            
            if e-j>=K:
                return quickSelect(A, j+1, e, K)
            elif e-i+1>=K:
                return pivot
            else:
                return quickSelect(A, s, i-1, K-(e-(i-1)))
            
        return quickSelect(nums, 0, len(nums)-1, K)