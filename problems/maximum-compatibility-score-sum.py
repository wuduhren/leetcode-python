"""
Time: O(ELogE), E is the edge of the graph.
Note that state[i] means if the ith student is matched or not. (for example M=4, 0000, 0010, 0111, 1111...)
2^M is the number of states. So in this case E will be 2^M x M.

Space: O(2^M)
"""
class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        M = len(students)
        N = len(students[0])

        #initialize reverseScores
        reverseScores = [[0]*M for _ in xrange(M)]
        for i in xrange(M):
            for j in xrange(M):
                reverseScore = 0
                for k in xrange(N):
                    if students[i][k]!=mentors[j][k]:
                        reverseScore += 1
                reverseScores[i][j] = reverseScore
        
        #Dijkstra
        startState = '0'*M
        endState = '1'*M
        visited = set()
        pq = [(0, startState)]
        
        while pq:
            cost, state = heapq.heappop(pq)
            if state in visited: continue
            visited.add(state)
            
            if state==endState: return M*N-cost
            
            j = state.count('1')
            for i in xrange(M):
                if state[i]=='1': continue
                
                nextState = state[:i]+'1'+state[i+1:]
                if nextState in visited: continue
                heapq.heappush(pq, (cost+reverseScores[i][j], nextState))
        
        return -1