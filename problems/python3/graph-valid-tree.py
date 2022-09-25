class Solution:
    def validTree(self, N: int, edges: List[List[int]]) -> bool:
        def union(n1, n2) -> bool:
            p1 = find(n1)
            p2 = find(n2)
            
            if p1==p2:
                return False
            elif p1<p2:
                parents[p2] = p1
            else:
                parents[p1] = p2
                
            return True
            
        
        def find(n) -> int:
            p = parents[n]
            while p!=parents[p]: p = find(p)
            parents[n] = p
            return p
        
        parents = [n for n in range(N)]

        for n1, n2 in edges:
            if not union(n1, n2): return False
        
        #check if all node trace back to the same root
        root = find(0)
        for n in range(1, N):
            if root!=find(n): return False
        
        return True