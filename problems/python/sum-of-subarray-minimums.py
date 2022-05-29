"""
[0]
Instead of listing iterate through all the subarrays (Which is O(N^2) in Time).
We think reversely.
For each num, how many subarrays such that the num is the minimum.
For each num, the count is (i-l) * (r-i)
Where l is the index of the first left number smaller to num.
Where r is the index of the first right number smaller to num.

[1]
To construct nextSmaller, we iterate through the number, if it is incremental, we put it in the stack.
Once we encounter a number that is "not" incremental, then it is the next smaller number of stack[-1].

[2]
Since there are some the same number in the arr. If we use nextSmaller and prevSmaller to calculate, there will be some subarrays repeatly counted.
So we need to set up boundaries. So that even with the same number, they will not count the same subarray.

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def sumSubarrayMins(self, arr):
        N = len(arr)
        ans = 0
        nextSmaller = [N]*N
        prevSmallerOrEqual = [-1]*N #[2]
        
        #construct nextSmaller [1]
        stack = []
        for i in xrange(N):
            n = arr[i]
            while stack and n<arr[stack[-1]]:
                nextSmaller[stack.pop()] = i
            stack.append(i)
        
        #construct prevSmallerOrEqual
        stack = []
        for i in xrange(N-1, -1, -1):
            n = arr[i]
            while stack and n<=arr[stack[-1]]:
                prevSmallerOrEqual[stack.pop()] = i
            stack.append(i)
        
        #get ans
        for i in xrange(N):
            n = arr[i]
            r = nextSmaller[i]
            l = prevSmallerOrEqual[i]
            ans += (i-l)*(r-i)*n #[0]
            
        return ans%(10**9+7)