class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        sortedCourse = []
        inbounds = collections.Counter()
        G = collections.defaultdict(list)
        q = collections.deque()
        
        for c1, c2 in prerequisites:
            G[c2].append(c1)
            inbounds[c1] += 1
        
        for c in range(numCourses):
            if inbounds[c]==0: q.append(c)

        while q:
            c = q.popleft()
            
            for c2 in G[c]:
                inbounds[c2] -= 1
                if inbounds[c2]==0: q.append(c2)    
            sortedCourse.append(c)
        
        return len(sortedCourse)==numCourses