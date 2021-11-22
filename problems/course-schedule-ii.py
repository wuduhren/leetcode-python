from collections import defaultdict, deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        inbound = defaultdict(int)
        q = deque()
        order = deque()
        
		#building graph as adjacency list
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            inbound[c1] += 1
        
		#find the starting point
        for c in xrange(numCourses):
            if inbound[c]==0:
                q.append(c)
        
		#traverse the directed graph
        while q:
            c = q.popleft()
            
            for nei in graph[c]:
                inbound[nei] -= 1
                if inbound[nei]==0:
                    q.append(nei)
                    
            order.append(c)
        
        return order if len(order)==numCourses else []

"""
Topological sort works only in directed graph.
We can use it to know which node comes after which or detect cycles.
The algorithm is easy to understand.
First, we build the adjacent list (`graph`) and count all the inbound of the node.
Then we start from the node whose inbound count is 0, adding it in to the `pq` (priority queue).
For every node we pop out from `pq`
    * We remove the node's outbound by decrease 1 on all its neighbor's inbound.
    * Put the node's neighbor to `pq` if it has no inbound
    * Put the node into the `sortedNodes`
Repeat the process until there is no more node.
The order in the `sortedNodes` is the order we are going to encounter when we run through the directed graph.
If we cannot sort all the nodes in the graph, it means that there are some nodes we couldn't find its starting point, in other words, there are cycles in the graph.

Time: O(E+2V) ~= O(E+V)
we used O(E) to build the graph #[1], O(V) to find the starting point #[2], then traverse all the nodes again #[3].
Space: O(E+3V) ~= O(E+V), O(E+V) for the adjacent list. O(V) for the `q`, O(V) for the `q_next`.
"""
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        inbounds = collections.defaultdict(int)
        pq = collections.deque()
        sortedNodes = []
        
        for c1, c2 in prerequisites:
            graph[c2].append(c1)
            inbounds[c1]+=1
        
        for node in xrange(numCourses):
            if inbounds[node]==0:
                pq.append(node)
        
        while pq:
            node = pq.popleft()
            
            for nei in graph[node]:
                inbounds[nei] -= 1
                if inbounds[nei]==0:
                    pq.append(nei)
            sortedNodes.append(node)
        
        return sortedNodes if len(sortedNodes)==numCourses else []
        