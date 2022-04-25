"""
Not sure how to scientifically prove this.
In order to turn all the 1 to 0, every row need to have "the same pattern". Or it is imposible.
This same pattern is means they are 1. identical 2. entirely different.
For example 101 and 101, 101 and 010.
110011 and 110011. 110011 and 001100.

Time: O(N), N is the number of element in the grid.
Space: O(N)
"""
class Solution(object):
    def removeOnes(self, grid):
        if not grid: return True
        rowStrings = set()
        
        for row in grid:
            rowStrings.add(''.join((str(e) for e in row)))
        
        if len(rowStrings)>2: return False
        if len(rowStrings)==1: return True
        
        s1 = rowStrings.pop()
        s2 = rowStrings.pop()
        
        for i in xrange(len(s1)):
            if (s1[i]=='0' and s2[i]=='1') or (s1[i]=='1' and s2[i]=='0'): continue
            return False
        return True