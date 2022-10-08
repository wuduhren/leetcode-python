"""
DFS with backtracking.
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(start) -> bool:
            if len(ans)==len(tickets)+1: return True
            if start not in adj: return False
            
            temp = list(adj[start])
            for i, arr in enumerate(temp):
                adj[start].pop(i)
                ans.append(arr)
                if dfs(arr): return True
                adj[start].insert(i, arr)
                ans.pop()
            return False
        
        ans = ['JFK']
        adj = collections.defaultdict(list)
        
        tickets.sort()
        for des, arr in tickets:
            adj[des].append(arr)
        
        dfs('JFK')
        return ans