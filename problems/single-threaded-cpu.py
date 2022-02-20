class Solution(object):
    def getOrder(self, tasks):
        ans = []
        tasks = sorted([(task[0], task[1], i) for i, task in enumerate(tasks)], reverse=True)
        pq = [] #tasks available
        now = 0
        
        
        while tasks or pq:
            #check if the task is availiable, if yes, add to pq
            while tasks and tasks[-1][0]<=now:
                startTime, processTime, i = tasks.pop()
                heapq.heappush(pq, (processTime, i))
                        
            if pq:
                processTime, i = heapq.heappop(pq)
                ans.append(i)
                now += processTime
            else:
                now = tasks[-1][0]
                    
        return ans