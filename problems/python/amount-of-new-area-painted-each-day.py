"""
1. Build sorted records = [(position, index, isStart)...]
2. Iterate through all positions and maintain a box with all the "index" of the records its position is in start ~ end
3. The smallest index in the box is the actual one that is paiting.

Time: O(NLogN+P), N is the count of paint. Sorting the records takes NLogN. P is the max position.
Although there is a while loop when iterate through P, each record is only being iterated once.
O(NLogN + P + NLogN) ~= O(NLogN + P)
Space: O(N)
"""
from sortedcontainers import SortedList

class Solution(object):
    def amountPainted(self, paint):
        ans = [0]*len(paint)
        box = SortedList()
        records = []
        maxPos = float('-inf')
        
        #[1]
        for i, (start, end) in enumerate(paint):
            records.append((start, i, -1))
            records.append((end, i, 1))
            maxPos = max(maxPos, end)
        
        records.sort()
        
        #[2]
        i = 0
        for pos in xrange(maxPos+1):
            while i<len(records) and records[i][0]==pos:
                _, index, t = records[i]
                if t==-1:
                    box.add(index)
                else:
                    box.remove(index)
                i += 1
            
            if box: ans[box[0]] += 1 #[3]
        return ans