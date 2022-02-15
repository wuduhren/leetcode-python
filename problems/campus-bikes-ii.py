"""
state[i] := ith bike has been selected.
For example, there are M bikes, 0000, 0100, 0110, 1111.....

Time: O(ELogE)
Space: O(E)
"""
class Solution(object):
    def assignBikes(self, workers, bikes):
        M = len(bikes)
        N = len(workers)
        costs = [[0]*N for _ in xrange(M)]
        
        for i in xrange(M):
            for j in xrange(N):
                costs[i][j] = abs(workers[j][0]-bikes[i][0])+abs(workers[j][1]-bikes[i][1])
        
        pq = [(0, '0'*M)]
        visited = set()
        while pq:
            cost, state = heapq.heappop(pq)
            if state in visited: continue
            visited.add(state)
            
            j = state.count('1') #j users have selected bikes
            if j>=N: return cost
            
            for i in xrange(M):
                if state[i]=='1': continue
                
                nextState = state[:i] + '1' + state[i+1:]
                if nextState in visited: continue
                heapq.heappush(pq, (cost+costs[i][j], nextState))
        
        return float('inf')