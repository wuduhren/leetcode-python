class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = {n:[] for n in xrange(numCourses)} #[0]
        
        for n1, n2 in prerequisites:
            graph[n1].append(n2)
        
        for target_course in xrange(numCourses): #[1]
            stack = graph[target_course]
            visited = set()
            while stack:
                course = stack.pop()
                visited.add(course)
                if course==target_course: return False
                for ajc in graph[course]:
                    if ajc not in visited:
                        stack.append(ajc)
        return True
"""
First, we build a graph of adjacency list #[0]
0->[2,4,5]
1->[3,4]
Meaning before taking 2,4,5 we need to take 0, before taking 3,4 we need to take 1
if we find a loop back to itself then it is impossible, for example
0->[2,4,5]
1->[3,4]
2->[0,3]
0->2->0, which is imposible.

Now we iterate every course to see if it can loop back to itself in anyway #[1]
we do this by dfs and search for it self
if we find itself we find loop

The time efficiency is O(V^2+VE), because each dfs in adjacency list is O(V+E) and we do it V times
Space efficiency is O(E).
V is the numCourses (Vertices).
E is the number of prerequisites (Edges).
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = collections.defaultdict(list)
        inbound = collections.defaultdict(int)
        q_next = collections.deque()
        q = collections.deque()

        for n1, n2 in prerequisites: #[1]
            graph[n1].append(n2)
            inbound[n2]+=1

        for n in xrange(numCourses): #[2]
            if inbound[n]==0:
                q_next.append(n)

        while q_next: #[3]
            n = q_next.popleft()
            for nei in graph[n]:
                inbound[nei]-=1
                if inbound[nei]==0:
                    q_next.append(nei)
            q.append(n)
        return len(q)==numCourses
        
"""
Topological sort works only in directed graph.
We can use it to know which node comes after which or detect cycles.
The algorithm is easy to understand.
First, we build the adjacent list and count all the inbound of the node.
Then we start from the node whose inbound count is 0, adding it in to the `q_next`.
For every node we pop out from q_next
    * We remove the node's outbound by decrease 1 on all its neighbor's inbound.
    * Put the node's neighbor to `q_next` if it has no inbound
    * Put the node into the `q`
Repeat the process until there is no more node.
The order in the `q` is the order we are going to encounter when we run through the directed graph.
If we cannot sort all the nodes in the graph, it means that there are some nodes we couldn't find its starting point, in other words, there are cycles in the graph.

Time: O(E+2V) ~= O(E+V)
we used O(E) to build the graph #[1], O(V) to find the starting point #[2], then traverse all the nodes again #[3].
Space: O(E+3V) ~= O(E+V), O(E+V) for the adjacent list. O(V) for the `q`, O(V) for the `q_next`.
"""