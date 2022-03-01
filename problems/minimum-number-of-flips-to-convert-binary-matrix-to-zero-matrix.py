class Solution(object):
    def minFlips(self, mat):
        def flip(mat, m, n):
            mat[m][n] = 0 if mat[m][n]==1 else 1
            if m+1<len(mat): mat[m+1][n] = 0 if mat[m+1][n]==1 else 1
            if n+1<len(mat[0]): mat[m][n+1] = 0 if mat[m][n+1]==1 else 1
            if m-1>=0: mat[m-1][n] = 0 if mat[m-1][n]==1 else 1
            if n-1>=0: mat[m][n-1] = 0 if mat[m][n-1]==1 else 1
            
        def check(mat, state):
            for i, b in enumerate(state):
                if b=='1':
                    m = i/len(mat[0])
                    n = i%len(mat[0])
                    flip(mat, m, n)
            
            for i in xrange(len(mat)):
                for j in xrange(len(mat[0])):
                    if mat[i][j]==1: return False
            
            return True
                    
        
        M = len(mat)
        N = len(mat[0])
        q = collections.deque(['0'*(M*N)])
        visited = set()
        
        while q:
            state = q.popleft()
            if state in visited: continue
            visited.add(state)
            
            if check([row[:] for row in mat], state): return state.count('1')
            
            for i in xrange(len(state)):
                if state[i]=='1': continue
                nextState = state[:i] + '1' +state[i+1:]
                q.append(nextState)
                
        return -1
    