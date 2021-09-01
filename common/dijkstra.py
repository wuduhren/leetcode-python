import heapq

"""
If we only want to find the shortest distance to the end and not all the nodes's shortest distance
The ending condition will be when `end` pop out from the `pq`.
And the path would be all the nodes that were popped out.
"""

#heap implementation
def min_path(G, start, end):
	distance = {}
	pq = []
	prev = {}
	path_str = ''
	visited = set()

	distance[start] = 0
	heapq.heappush(pq, (0, start))

	while pq:
		dis_to_mid, mid = heapq.heappop(pq)
		visited.add(mid)

		for dis, nei in G[mid]:
			if nei not in distance or distance[nei]>dis_to_mid+dis:
				distance[nei] = dis_to_mid+dis
				prev[nei] = mid
				if nei not in visited:
					heapq.heappush(pq, (distance[nei], nei))

	curr = end
	while True:
		if curr not in prev: break
		path_str = ' -> '+prev[curr]+path_str
		curr = prev[curr]

	return path_str+' = '+str(distance[end])



#normal implementation
def min_path(G, start, end):
	distance = {} #shortest distance from start
	prev = {}
	path_str = ''
	visited = set()

	distance[start] = 0
	while True:
		#find nearest unvisited node
		mid = None
		dis_to_mid = float('inf')
		for node in distance:
			if node not in visited and distance[node]<dis_to_mid:
				mid = node
				dis_to_mid = distance[node]

		if mid==None: break
		visited.add(mid)

		#try to use mid to loosen the prev from start to mid's neighbors
		for dis, nei in G[mid]:
			if nei not in distance or dis_to_mid+dis<distance[nei]:
				distance[nei] = dis_to_mid+dis
				prev[nei] = mid

	curr = end
	while True:
		if curr not in prev: break
		path_str = ' -> '+prev[curr]+path_str
		curr = prev[curr]

	print path_str+' = '+str(distance[end])

G = {
	'0': [(1, '1'), (12, '2')],
	'1': [(9, '2'), (3, '3')],
	'2': [(5, '4')],
	'3': [(4, '2'), (13, '4'), (15, '5')],
	'4': [(4, '5')],
	'5': []
}

print min_path(G, '0', '5')



