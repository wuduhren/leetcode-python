"""
We use the `roots` to store the root of each node.
For example, at index 1 value is 5, means that node1's root is node5.

We use `find()` to find the node's root. In other words, the node's parent's parent's ...
Every node we encounter along the way, we update their root value in `roots` to the up most root. (This technique is called path compression).

So, for every edge, we unify `u` and `v` them. #[1]
Which means u and v and all of their parents all lead to one root.

If u's root (`ur`) and v's root (`vr`) are already the same before we unify them.
This edge is redundant.

This algorithm is called Union Find, often used in undirected graph cycle detect or grouping.
If you wanted to detect cycles in directed graph, you need to use Topological sort.
"""
class Solution(object):
    def findRedundantConnection(self, edges):
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]

        opt = []
        roots = range(len(edges))

        for u, v in edges:
            # union
            ur = find(u)
            vr = find(v)

            if ur == vr: #[2]
                opt = [u, v]
            else:
                roots[vr] = ur #[1]

        return opt