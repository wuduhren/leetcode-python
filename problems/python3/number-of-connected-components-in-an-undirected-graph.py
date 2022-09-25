class Solution:
    def countComponents(self, N: int, edges: List[List[int]]) -> int:
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return
            elif p1<p2:
                parents[p2] = p1
            else:
                parents[p1] = p2
            
        def find(n):
            p = parents[n]
            while p!=parents[p]: p = find(p)
            parents[n] = p
            return p
        
        parents = {n:n for n in range(N)}
        for n1, n2 in edges: union(n1, n2)
        
        groups = set()
        for n in range(N): groups.add(find(n))
            
        return len(groups)