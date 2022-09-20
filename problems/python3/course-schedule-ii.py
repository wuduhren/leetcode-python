#Topological Sort
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sortedCourse = []
        G = collections.defaultdict(list) #graph
        inbounds = collections.Counter()
        q = collections.deque()
        
        #build graph
        for c1, c2 in prerequisites:
            G[c2].append(c1)
            inbounds[c1] += 1
        
        #add the starting point to the q. (the ones that have 0 inbounds)
        for course in range(numCourses):
            if inbounds[course]==0: q.append(course)
        
        #add the course that have 0 inbounds to the sortedCourse.
        #after that, imagine we remove it from the graph, so nextCourse inbound will -1
        #add to q if nextCourse have 0 inbounds
        while q:
            course = q.popleft()
            
            sortedCourse.append(course)
            
            for nextCourse in G[course]:
                inbounds[nextCourse] -= 1
                if inbounds[nextCourse]==0: q.append(nextCourse)
        
        return sortedCourse if len(sortedCourse)==numCourses else []