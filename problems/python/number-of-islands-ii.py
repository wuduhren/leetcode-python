"""
For each new land, the count will -= ((number of neighbors) - 1).
Because some for this new land introduced, some of the separate islands will be connected.
Note that, "number of neighbors", islands connected does not count. So for each neighbor, we use "find" to find its root.
"""
class Solution(object):
    def numIslands2(self, M, N, positions):
        def coorToNum(r, c):
            return N*r+c
        
        def find(n):
            p = parents[n]
            while p!=parents[p]:
                p = find(p)
            parents[n] = p
            return parents[n]
            
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1==p2: return
            parents[p1] = p2
            
        count = 0
        lands = set()
        ans = []
        parents = [n for n in xrange(M*N)]
        
        for r, c in positions:
            n = coorToNum(r, c)
            
            if n in lands:
                ans.append(count)
                continue
            
            neis = set()
            if r+1<M and coorToNum(r+1, c) in lands: neis.add(find(coorToNum(r+1, c)))
            if 0<=r-1 and coorToNum(r-1, c) in lands: neis.add(find(coorToNum(r-1, c)))
            if c+1<N and coorToNum(r, c+1) in lands: neis.add(find(coorToNum(r, c+1)))
            if 0<=c-1 and coorToNum(r, c-1) in lands: neis.add(find(coorToNum(r, c-1)))
                
            count -= (len(neis)-1)
            lands.add(n)
            ans.append(count)
            
            for nei in neis:
                union(n, nei)
            
        return ans