"""
First, set the distance to 0 when `i` and `j` in the `matrix` is 0. [0]

Second, when an `(i, j)` in the `opt` is 0, its neighbor's distance is 0+1, so
we set all the `i` and `j` in the `opt` where its distance is 1.
then set all the `i` and `j` in the `opt` where its distance is 2.
then set all the `i` and `j` in the `opt` where its distance is 3.
then set all the `i` and `j` in the `opt` where its distance is 4.
...

the `count` is the number of distance that we found.
While we haven't find all the answer, we keep on doing above operation. [1]

The time comlexity is `O(N^2)`, **N is the number of element in the 2D matrix**.
The space complexity is `O(N)`, where we store the `opt`.
"""
class Solution(object):
    def updateMatrix(self, matrix):
        def setDistance(i, j, dis):
            if i<0 or i>=M: return False
            if j<0 or j>=N: return False
            if opt[i][j]!=-1: return False #opt[i][j]==-1 means the value is set already, skip.
            opt[i][j] = dis
            return True

        M, N = len(matrix), len(matrix[0])
        opt = [[-1]*N for _ in xrange(M)]
        dis = 0
        count = 0

        #[0]
        for i in xrange(M):
            for j in xrange(N):
                if matrix[i][j]==0:
                    count+=1
                    opt[i][j] = 0

        while count<M*N:
            for i in xrange(M):
                for j in xrange(N):
                    if opt[i][j]==dis:
                        if setDistance(i+1, j, dis+1): count+=1
                        if setDistance(i-1, j, dis+1): count+=1
                        if setDistance(i, j+1, dis+1): count+=1
                        if setDistance(i, j-1, dis+1): count+=1
            dis+=1
        return opt

"""
Standard BFS
The same idea, but use BFS to implement.
The time complexity is `O(N)`, **N is the number of element in the 2D matrix**.
The space complexity is `O(N)`, where we store the `opt`.
"""
class Solution(object):
    def updateMatrix(self, matrix):
        M, N = len(matrix), len(matrix[0])
        opt = [[-1]*N for _ in xrange(M)]
        q = collections.deque([])

        for i in xrange(M):
            for j in xrange(N):
                if matrix[i][j]==0:
                    q.append((i, j, 0))

        while q:
            i, j, dis = q.popleft()
            if i<0 or i>=M: continue
            if j<0 or j>=N: continue
            if opt[i][j]!=-1: continue
            opt[i][j] = dis

            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                q.append((ni, nj, dis+1))

        return opt



