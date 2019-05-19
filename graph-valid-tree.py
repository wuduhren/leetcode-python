"""
First of all a tree of N nodes must have exactly N-1 edges.
2 nodes need 1 edge to connect. 3 nodes need 2 edges to connect...
Just draw one or two, you will know it.

Valid tree don't have cycles, there are two ways to detect it.
DFS. and union find. Union find is more suitable in this sutuation.

1. Union find.
We use an array 'markset' to store the root node of each node. [0]
So if markset[1]==3, it means node1's root is node3.
markset[6]==4, node6's root is node4.

we use find() to find the node's root. [1]
For example if node1's root is node3.
In the recursion, we find out that node3's root is node5.
we return and set node5 as node1's real root.
If a node don't have root then the root is itselves.

Imagine an edge. 1<->6 [2]
union()'s mission is to find out if node1 and node6 share the same root before we know 1<->6 exist.
If node1 and node6 share the same root before we know the edge 1<->6, 
There must be a cycle between node1, node6 and their root.

A special situation is that
1<->2, 3<->4, 3<->5 (We have two trees that are not connected)
1 and 3 will share -1 as 'root', this means that they are not connected.
But a valid tree should be connected and only have one and only root.

The time complexity is O(NLogN), becuase we run a loop for every edges.
And the number of edges is equal to N-1
for every edge we use find() to find the root of two nodes
The recursion takes the height of the tree, which is LogN
N is the number of nodes.

Space complexity is O(N).

2. DFS
We use dfs to find if there are cycles in the tree.
If we visit the node that we visited which means there is a cycle.
Since this is an undirected map, we have to add both ways to the adjacent list.
And everytime we use an edge, we need to remove the counter part of it to avoid repeat.
finally, we have to check if we visit all the nodes. because there may be unconnected nodes.

The time complexity is O(N+E). Because this is DFS search in adjacent list.
Space complexity is O(N).
"""
class Solution(object):
	def validTree(self, n, edges):
		def union(n1, n2): #[2]
			n1_root = find(n1)
			n2_root = find(n2)
			if n1_root==n2_root: return True
			markset[n2_root] = n1_root
			return False

		def find(node): #[1]
			if markset[node]==-1: return node
			return find(markset[node])

		if len(edges)!=n-1: return False
		markset = [-1 for _ in xrange(n)] #[0]

		for edge in edges:
			if union(edge[0], edge[1]): return False

		return True


    def validTree(self, n, edges):
		if n!=len(edges)+1: return False

		graph = collections.defaultdict(list)
		stack = []
		visited = set()

		for edge in edges:
			graph[edge[0]].append(edge[1])
			graph[edge[1]].append(edge[0])

		if len(edges)>0:
			stack.append(edges[0][0])

			while stack:
				node = stack.pop()
				if node in visited: return False
				visited.add(node)
				for nb in graph[node]:
					stack.append(nb)
					graph[nb].remove(node)

			if len(visited)!=n: return False

		return True
