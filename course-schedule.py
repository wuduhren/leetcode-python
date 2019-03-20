"""
we build a graph of adjacency list, like [0]
0->[2,4,5]
1->[3,4]
meaning before taking 2,4,5 we need to take 0, before taking 3,4 we need to take 1
if we find a loop back to itself then it is impossible, for example
0->[2,4,5]
1->[3,4]
2->[0,3]
0->2->0, which is imposible

now we iterate every course to see if it can loop back to itself in anyway [1]
we do this by dfs and search for it self
if we find itself we find loop

the time efficiency is O(V^2+VE), bc each dfs in adjacency list is O(V+E) and we do it V times
space efficiency is O(E)
V is the numCourses(Vertices)
E is the prerequisites(Edges)
"""
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