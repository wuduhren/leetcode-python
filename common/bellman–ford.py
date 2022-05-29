"""
First, we use `distance` to track the distance from start to all others.
For V nodes, it takes at least V-1 iteration to complete the algorithm.
For every iteration,
We use every node as the middle point to see if it can "loosen" the path from start to mid to mid's neighbors
If it can loosen the path, we update the `distance`.
The time complexity is O(VE)
"""
def min_path(G, N, start, end):
    distance = [float('inf') for _ in xrange(N+1)]
    distance[start] = 0

    for _ in xrange(N-1):
        for mid, dis in enumerate(distance):
            if dis==float('inf'): continue
            for dis_to_nei, nei in G[mid]:
                distance[nei] = min(distance[nei], dis+dis_to_nei)
    return distance[end]


G = {
    0: [(-2, 1), (4, 2)],
    1: [(5, 2)],
    2: [(12, 3), (5, 4)],
    3: [(-8, 4)],
    4: []
}
N = 4 #nodes count
start = 0
end = 4
print min_path(G, N, start, end)
