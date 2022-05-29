class Solution(object):
    def minimumCost(self, N, connections):
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1==p2: return False
                
            if ranks[p1]>ranks[p2]:
                parents[p2] = p1
                ranks[p1] += 1
            else:
                parents[p1] = p2
                ranks[p2] += 1
            return True

        def find(n):
            p = parents[n]
            while p!=parents[p]: p = find(p)
            parents[n] = p
            return p
        
        if not connections: return 0
        
        parents = [n for n in xrange(N+1)]
        ranks = [0]*(N+1)
        totalCost = 0
        count = N # the count of nodes not yet union
        
		# sort by cost, union the ones with less cost first
        sortedConnections = sorted([(cost, x, y) for x, y, cost in connections])
        
        for cost, x, y in sortedConnections:
            if union(x, y):
                totalCost += cost
                count -= 1
                 
        return totalCost if count==1 else -1