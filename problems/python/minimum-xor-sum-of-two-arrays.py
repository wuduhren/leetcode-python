"""
state[i] := nums1[i] has been matched.
"""
class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        N = len(nums1)
        
        pq = [(0, '0'*N)]
        visited = set()
        while pq:
            s, state = heapq.heappop(pq)
            if state in visited: continue
            visited.add(state)
            
            j = state.count('1')
            if j==N: return s
            
            for i in xrange(N):
                if state[i]=='1': continue
                nextState = state[:i]+'1'+state[i+1:]
                if nextState in visited: continue
                heapq.heappush(pq, ((s+(nums1[i]^nums2[j-1]), nextState)))
        
        return float('inf')