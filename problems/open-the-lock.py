"""
In priority queue, we not only take `steps` in to consideration but also `distance`
And the rest is just like dijkstra.
"""
import heapq
class Solution(object):
    def openLock(self, deadends, target):
        def getNeighbor(node):
            opt = []
            for i in xrange(len(node)):
                if node[i]==0:
                    opt.append(tuple(node[:i]+(1,)+node[i+1:]))
                    opt.append(tuple(node[:i]+(9,)+node[i+1:]))
                elif node[i]==9:
                    opt.append(tuple(node[:i]+(0,)+node[i+1:]))
                    opt.append(tuple(node[:i]+(8,)+node[i+1:]))
                else:
                    opt.append(tuple(node[:i]+(node[i]+1,)+node[i+1:]))
                    opt.append(tuple(node[:i]+(node[i]-1,)+node[i+1:]))
            return opt

        def getDistance(node):
            distance = 0
            for i in xrange(len(node)):
                d = abs(int(node[i])-int(target[i]))
                d2 = abs(10-d)
                distance+=min(d, d2)
            return distance

        def tupify(node):
            return tuple(map(int, node))

        target = tupify(target)
        visited = set([tupify(node) for node in deadends])
        pq = [(0, 0, tupify('0000'))]

        while pq:
            _, steps, node = heapq.heappop(pq)
            if node==target: return steps
            if node in visited: continue
            visited.add(node)
            for nei in getNeighbor(node):
                heapq.heappush(pq, (steps+1+getDistance(nei), steps+1, nei))
        return -1

class Solution:
    def openLock(self, deadends, target):
        def getNeighbor(node):
            opt = []
            for i in xrange(len(node)):
                add_one = delta[node[i]][0]
                minus_one = delta[node[i]][1]
                opt.append(node[:i]+add_one+node[i+1:])
                opt.append(node[:i]+minus_one+node[i + 1:])
            return opt

        delta = {str(i): [str((i+1)%10), str((i-1)%10)] for i in xrange(10)}
        visited = set(deadends)
        q = collections.deque([('0000', 0)])
        steps = 0

        while q:
            node, steps = q.popleft()
            if node==target: return steps
            if node in visited: continue
            visited.add(node)
            for nei in getNeighbor(node):
                q.append((nei, steps+1))

        return -1
