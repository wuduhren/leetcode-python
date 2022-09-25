class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            
            if p1==p2:
                return False #union failed, already united.
            elif p1<p2:
                roots[p2] = p1
            else:
                roots[p1] = p2
        
            return True #union success
        
        def find(n):
            if n not in roots:
                roots[n] = n
                return n
            
            p = roots[n]
            while p!=roots[p]:
                p = find(p)
            roots[n] = p
            return p
        
        roots = {}
        
        for n1, n2 in edges:
            if not union(n1, n2): return (n1, n2)
        
        return 'ERROR'