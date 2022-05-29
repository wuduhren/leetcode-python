from collections import defaultdict, deque

class Solution(object):
    def eventualSafeNodes(self, graph):
        inbounds = defaultdict(list)
        outbondsCounter = defaultdict(int)
        q = deque()
        ans = []
        
        for n, nei_list in enumerate(graph):
            outbondsCounter[n] = len(nei_list)
            for nei in nei_list:
                inbounds[nei].append(n)
        
        for n in outbondsCounter:
            if outbondsCounter[n]==0:
                q.append(n)
        
        while q:
            n = q.popleft()

            for nei in inbounds[n]:
                outbondsCounter[nei] -= 1
                if outbondsCounter[nei]==0:
                    q.append(nei)
            
            ans.append(n)
        
        return ans.sort()