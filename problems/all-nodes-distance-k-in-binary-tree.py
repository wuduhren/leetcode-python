class Solution(object):
    def distanceK(self, root, target, k):
        graph = collections.defaultdict(list)
        q = collections.deque([root]) #for traverse binary tree
        q2 = collections.deque([(target, k)]) #for bfs the graph
        visited = set() #for bfs the graph
        ans = []
        
        #build graph
        while q:
            node = q.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                q.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                q.append(node.right)
        
        
        #bfs graph
        while q2:
            node, distance = q2.popleft()
            if node.val in visited: continue
            visited.add(node.val)
            if distance==0: ans.append(node.val)
            if distance<0 or distance>k: continue
            
            for nei in graph[node]:
                q2.append((nei, distance-1))
        
        return ans
            
            
            
            
        