"""
For each "island" asign them a group id. Also calculate the group's size.
Iterate all the zeros, update the ans.

Time:O(MN)
Space: O(MN) in the worst case.
"""
class Solution(object):
    def largestIsland(self, grid):
        def isValid(i, j, M, N):
            return 0<=i<M and 0<=j<N
        
        def dfs(i, j, groupId):
            if not isValid(i, j, M, N): return
            if grid[i][j]!=1: return
            grid[i][j] = groupId
            groupIdToSize[groupId] += 1
            for iNext, jNext in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                dfs(iNext, jNext, groupId)

        M = len(grid)
        N = len(grid[0])
        
        zeros = []
        groupIdToSize = {}
        groupId = 2
        for i in xrange(M):
            for j in xrange(N):
                if grid[i][j]==1:
                    groupIdToSize[groupId] = 0
                    dfs(i, j, groupId)
                    groupId += 1
                elif grid[i][j]==0:
                    zeros.append((i, j))
                    
        ans = max(groupIdToSize.values()) if groupIdToSize else 0
        
        for i, j in zeros:
            neiGroupId = set()
            neiSize = 0
            for iNext, jNext in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if not isValid(iNext, jNext, M, N): continue
                if grid[iNext][jNext]>1:
                    neiGroupId.add(grid[iNext][jNext])
            
            for groupId in list(neiGroupId):
                neiSize += groupIdToSize[groupId]
            
            ans = max(ans, 1+neiSize)
        
        return ans