class Solution(object):
    def maxSlidingWindow(self, nums, k):
        opt = []
        q = collections.deque()
        for i in xrange(len(nums)):
            n = nums[i]
            
            #move the window
            if q and q[0]<=i-k: q.popleft()

            #pop the right if the element in queue is not greater than the in-coming one
            #by doing this, we can always keep the max in the current window at left most
            while q and nums[q[-1]]<=n: q.pop()

            q.append(i)

            #add the max to the output array after the first kth element
            if 1+i>=k: opt.append(nums[q[0]])
        return opt


"""
Keep the element in sliding window in a heap, so we can get the max easily.
But we do not know whether which element in the heap is out of the window.
So we use a counter to track the count of the elements inside the window.

Time: O(NLogK), the `heapq.heappop(h)` in the while-loop in the for-loop will only be execute once for each element.
Space: O(N)
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or not k: return []
        if k==1: return nums
        
        ans = []
        
        counter = collections.Counter(nums[:k])
        h = [-num for num in nums[:k]]
        heapq.heapify(h)
        
        for i in xrange(len(nums)):    
            while counter[-h[0]]==0: heapq.heappop(h)
            ans.append(-h[0])
            
            if i+k>=len(nums): break
            counter[nums[i]] -= 1
            heapq.heappush(h, -nums[i+k])
            counter[nums[i+k]] += 1
        
        return ans

"""
Use deque the slide the window through nums.
The deque will at most contain k elements.
Each time add the max element to ans.

Time: O(N), the `q.pop()` in the while-loop in the for-loop will only execute once for each element.
Space: O(N)
"""
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        q = collections.deque()
        
        for i, num in enumerate(nums):
            #keep only the element in the window inside deque.
            #the window lies between index i-k+1 to i.
            if q and q[0][1]<=i-k: q.popleft()
            
            #keep the element in deque in descending order by popping the elements from rihgt that are smaller than num.
            #by keeping the deque in descending order, we can get the largest element by just getting the first element.
            #also since they are certainly not the max in the deque, we don't care.
            while q and q[-1][0]<=num: q.pop()
            q.append((num, i))
            
            #wait until i>=k-1 when the window pass at least k elements.
            if (i>=k-1): ans.append(q[0][0])
                
        return ans