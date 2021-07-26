"""
Time: O(LogN)
Space: O(1)

This problem is very similar to problem 278.

`l` is the lower bound of the possible numbers.
`h` is the higher bound of the possible numbers.
We always `guess` the number in the middle of `l` and `h`, which is `m`.
If the result (`r`) of `guess(m)` is 0, we found the answer. Return `m`.
If the result is 1, we know that the answer is larger than m, so the lower bound (`l`) is now m+1.
If the result is -1, we know that the answer is smaller than m, so the higher bound (`h`) is now m-1.
"""
class Solution(object):
    def guessNumber(self, n):
        l = 1
        h = n
        
        while l<h:
            m = (l+h)/2    
            
            r = guess(m)
            
            if r==0:
                return m
            elif r==1:
                l = m+1
            elif r==-1:
                h = m-1
                
        return (l+h)/2