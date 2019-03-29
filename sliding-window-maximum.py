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