"""
Dijkstra's algorithm heap implementation
first, we build an adjacent list. [0]
if you don't know what is adjacent list, see https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

we use a hash-map 'dis' to keep track of every node's distance to K. [1]
and we use a priority queue 'pq' to store all the node we encounter and its distance to K. [2]
which we use a tuple (distance to K, node)

for every node we visit, if its distance to K is determined, we don't need to look at it anymore. [3]
because we always pop the nearest one to the K in the priority queue, we can be sure that the distance in 'dis' is the shortest.
then from the node, which we know the shortest path from K to the node, we keep on explore its neighbors. [4]

then if we didn't visit every node we return -1, else we return the node which it takes the longest time to reach. [5]

for time complexity
we use O(E) to make an adjacency list from edge list.
we will go through the while loop V-1 times because we need to determined the distance of V-1 other nodes.
for every loop 
    we pop from priority queue (here need O(logE) to get the nearest node).
    we push the node's neighbor to the priority queue d times (which is the degree of the node)
    push the node takes O(logE), we assume all the node is in the queue.
    so every loop we use O(d*logE+logE)~=O(d*logE)
so total for total, it is O((V-1)*(d*logE))+O(E), we know that V-1~=V and V*d=E
so it is O(ElogE)+O(E)~=O(ElogE)
E is the number of edges, which is the length of 'times' of the input
V is the number of node, which is the 'N' of the inout

for space complexity
we used O(V) and O(E) in 'dis' and 'pq', and O(E) on the adjacency list.
so, it is O(V+E).
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        aj_list = collections.defaultdict(list) #[0]
        for u, v, w in times: 
            aj_list[u].append((w, v))
        
        dis = {} #[1]
        pq = [(0, K)] #[2]
        
        while pq:
            if len(dis)==N: break

            d, node = heapq.heappop(pq)
            if node in dis: continue #[3]

            dis[node] = d
            
            for d2, nb in aj_list[node]: #[4]
                if nb not in dis: #[3]
                    heapq.heappush(pq, (d+d2, nb)) #[2]
                    
        return max(dis.values()) if len(dis)==N else -1 #[5]


#2020/10/17
class Solution(object):
    def networkDelayTime(self, times, N, K):
        ans = float('-inf')
        h = [(0, K)]
        visited = set()
        G = collections.defaultdict(list)
        
        for u, v, w in times:
            G[u].append((v, w))
        
        while h:
            time, node = heapq.heappop(h)
            
            if node in visited: continue
            visited.add(node)
            ans = max(ans, time)
            
            if len(visited)==N: return time
            for nei, time_to_nei in G[node]:
                heapq.heappush(h, (time+time_to_nei, nei))
        
        return -1

