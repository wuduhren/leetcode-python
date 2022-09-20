class Solution:
    def cloneGraph(self, start: 'Node') -> 'Node':
        def dfs(node):
            if node in clones: return clones[node]
            
            copy = Node(node.val)
            clones[node] = copy
            
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return clones[node]
        if not start: return start
        clones = {}
        dfs(start)
        return clones[start]