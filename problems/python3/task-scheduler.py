class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = collections.deque()
        h = []
        time = 0
        
        counter = collections.Counter(tasks)
        for task in counter:
            heapq.heappush(h, (-counter[task], task))
        
        while h or q:
            if q and q[0][0]<=time:
                _, count, task = q.popleft()
                heapq.heappush(h, (-count, task))
            
            if h:
                count, task = heapq.heappop(h)
                count*=-1
                count -= 1
                if count>0: q.append((time+n+1, count, task))
            time += 1
        
        return time