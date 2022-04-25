class Solution(object):
    def findCircleNum(self, isConnected):
        def bfs(startNode):
            q = collections.deque([startNode])
            
            while q:
                node = q.popleft()
                if node in visited: continue
                visited.add(node)
                
                for nei in xrange(N):
                    if nei!=node and isConnected[node][nei]==1:
                        q.append(nei)
        
        N = len(isConnected)
        visited = set()
        ans = 0
        
        for node in xrange(N):
            if node in visited: continue
            bfs(node) #put all the nodes in the same province to visited
            ans += 1
                    
        return ans