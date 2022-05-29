"""
We know that, after swapping, the length of the continuous 1 will be equal to number of 1 in the data. Let's call it `L`.
So what we need to do is sliding window with length L and see what is the max 1 count within the window.
The window with max 1 count will need to do minimal swap.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def minSwaps(self, data):
        L = 0 #sliding window length
        #initialize L
        for num in data:
            if num==1: L += 1
        
        count = 0 #count of 1 within the sliding window
        maxCount = 0 #max count of 1 within the sliding window

        #initialize the count from data[0] to data[L-1]
        for i in xrange(L):
            if data[i]==1: count += 1
        maxCount = count

        #slide the window
        for i in xrange(1, len(data)):
            #i: start index of the sliding window
            j = i+L-1 #end index of the sliding window
            if j>=len(data): break
            if data[j]==1: count += 1
            if data[i-1]==1: count -= 1
            maxCount = max(maxCount, count)
        
        return L-maxCount