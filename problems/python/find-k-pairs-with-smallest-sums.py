"""
Time: O(kLogk)
Space: O(N)

[0]
Declare a min-heap. Which stores the (sum, index in nums1, index in nums2) for each combination.

[1]
Each iteration, we get a min sum (i, j) from the heap and add it to the `ans`.
The next possible smallest combination will be either (i+1, j) or (j+1, i) or other combination previously added.
Add combination (i+1, j) and (j+1, i) to the heap.

[2]
Use a set `seen` to avoid adding the same element to the heap.
For example (i+1, j) and (j+1, i) can both lead to (i+1, j+1).
"""
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2: return []
        if k>len(nums1)*len(nums2): k = len(nums1)*len(nums2)
            
        ans = []
        h = [(nums1[0]+nums2[0], 0, 0)] #[0]
        seen = set([(0,0)]) #[2]
        
        while len(ans)<k: #[1]
            s, i, j = heapq.heappop(h)
            ans.append((nums1[i], nums2[j]))

            if i+1<len(nums1) and (i+1, j) not in seen:
                heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
                seen.add((i+1, j))

            if j+1<len(nums2) and (i, j+1) not in seen:
                heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
                seen.add((i, j+1))
                
        return ans