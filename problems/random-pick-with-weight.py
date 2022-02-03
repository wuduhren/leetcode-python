"""
For W = [1,3,2,4] (total 10, 1+2+3+4)
Think of a line _,___,__,____ ([1,4,6,10])
Now we randomly throw a ball on the line the probability to land on the first section will be 1/10.
the second section, 3/10.
the third section, 2/10.
the forth section, 4/10.

Above is equivilant to we randomly pick a number [0~10) and see which section it is in.
And since the cumulative probability in the "line" is strictly increasing, we can use binary search.

Time: O(LogN), N is the number of W.
Space: O(N).
"""
from random import randrange

class Solution(object):

    def __init__(self, W):
        self.line = [] #cumulative probability distribution
        self.total = 0
        
        for w in W:
            self.total += w
            self.line.append(self.total)

    def pickIndex(self):
        rand = random.randrange(self.total)
        return bisect.bisect(self.line, rand)