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
        #to be continued...
        pass