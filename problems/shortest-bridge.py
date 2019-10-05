import collections
class Solution(object):
    def shortestBridge(self, A):
        def findFirst():
            for i in xrange(M):
                for j in xrange(N):
                    if A[i][j]==1: return (i, j)

        M, N = len(A), len(A[0])
        opt = float('inf')

        q1 = collections.deque([findFirst()])
        while q1:
            i, j = q1.popleft()
            if i<0 or i>=M: continue
            if j<0 or j>=N: continue
            if A[i][j]==2 or A[i][j]==0: continue
            if A[i][j]==1: A[i][j] = 2
            q1.extend([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])

        i0, j0 = findFirst()
        q2 = collections.deque([(i0, j0, 0)])
        while q2:
            i, j, dis = q2.popleft()
            if A[i][j]==3 or A[i][j]==4:
                continue
            if A[i][j]==2:
                opt = min(opt, dis)
                continue

            if A[i][j]==1: A[i][j] = 3
            if A[i][j]==0: A[i][j] = 4
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if ni<0 or ni>=M: continue
                if nj<0 or nj>=N: continue
                if A[ni][nj]==1:
                    q2.append((ni, nj, 0))
                elif A[ni][nj]==0:
                    q2.append((ni, nj, dis+1))
                elif A[ni][nj]==2:
                    q2.append((ni, nj, dis))

        return opt

A = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,0],[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0]]
print Solution().shortestBridge(A)




