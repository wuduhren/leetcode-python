"""
Max stones can be remove = number of stones - number of groups
The stone in the same group has the same row or col with any stone in the group.
Since finding stones in the same group will take O(N^2)
Instead, we union the row or col itself.

So initially each col (c1, c2...) and row (r1, r2...)'s parent is itself.
We iterate through the stones and union the col and row.
For example, the stone (1, 2) will union r2 and c1.
the stone (0, 3) will union r3 and c0.
...

This way, we can also get the number of groups.

See better explanation in https://www.youtube.com/watch?v=beOCN7G4h-M

Time: O(N).
Space: O(N)
"""
class Solution(object):
    def removeStones(self, stones):
        def union(x, y):
            row = 'r'+str(x)
            col = 'c'+str(y)
            p1 = find(row)
            p2 = find(col)
            if p1==p2: return False
            parents[p2] = p1
            return True
        
        def find(c):
            p = parents[c]
            while p!=parents[p]:
                p = find(p)
            parents[c] = p
            return p
        
        parents = {}
        for x, y in stones:
            row = 'r'+str(x)
            col = 'c'+str(y)
            parents[row] = row
            parents[col] = col
        
        groupCount = len(parents)
        for x, y in stones:
            if union(x, y): groupCount -= 1
        
        return len(stones)-groupCount