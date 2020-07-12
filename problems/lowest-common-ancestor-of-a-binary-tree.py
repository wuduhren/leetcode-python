class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p_ancestor = []
        q_ancestor = []

        stack = []
        stack.append((root, []))
        while stack:
            node, path = stack.pop()
            if node is p: p_ancestor = path+[p]
            if node is q: q_ancestor = path+[q]
            if p_ancestor and q_ancestor: break #[0]
            if node.left: stack.append((node.left, path+[node]))
            if node.right: stack.append((node.right, path+[node]))
        
        if len(p_ancestor)>len(q_ancestor): #[1]
            s = set(q_ancestor)
            for node in reversed(p_ancestor): #[2]
                if node in s: return node #[3]
        else: #[1]
            s = set(p_ancestor)
            for node in reversed(q_ancestor): #[2]
                if node in s: return node #[3]
        return None



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def helper(node):
            if not node: return False
            l, r = helper(node.left), helper(node.right)
            curr = node is p or node is q
            if (int(l)+int(r)+int(curr) >= 2): self.ans = node
            return l or r or curr
        
        self.ans = None
        helper(root)
        return self.ans



class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        stack = []
        stack.append(root)

        parent = {}
        parent[root] = None

        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
        
        p_ancestor = p
        q_ancestor = q
        p_ancestors = set()
        while p_ancestor:
            p_ancestors.add(p_ancestor)
            p_ancestor = parent[p]
        while q_ancestor:
            if q_ancestor in p_ancestors: return q_ancestor
            q_ancestor = parent[q]
            
        return None


#2020/7/11
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def find_genealogy():
            genealogy = {}
            stack = []
            stack.append(root)
            p_found = q_found = False
            while stack:
                node = stack.pop()
                if node.left:
                    genealogy[node.left] = node
                    stack.append(node.left)
                if node.right:
                    genealogy[node.right] = node
                    stack.append(node.right)
    
                if node is p: p_found = True
                if node is q: q_found = True
                if p_found and q_found: break
            return genealogy

        def find_ancestors(target, genealogy):
            ancestors = []
            curr_node = target
            while curr_node:
                ancestors.append(curr_node)
                curr_node = genealogy[curr_node] if curr_node in genealogy else None
            return ancestors

        def find_lowest_common(a1, a2):
            if len(a1)>len(a2):
                a2 = set(a2)
                for node in a1:
                    if node in a2:
                        return node
            else:
                a1 = set(a1)
                for node in a2:
                    if node in a1:
                        return node

        genealogy = find_genealogy()
        p_ancestors = find_ancestors(p, genealogy)
        q_ancestors = find_ancestors(q, genealogy)
        return find_lowest_common(p_ancestors, q_ancestors)

"""
The idea is simple
Find all the ancestors of `p` and `q`.
To find ancestors of `p` and `q`, we need to generate a `genealogy`, where we can find the parant of each node. (genealogy[child] = parant)
After that, we see if the lowest node exist in both `p_ancestor` and `q_ancestor`.
To make sure we start from the lowest node, we need to start from the larger `p_ancestor` or `q_ancestor`.

Time complexity: O(N).
find_genealogy() is O(N), because we use DFS  to travel all nodes.
find_ancestors() is O(LogN).
find_lowest_common is O(LogN).
Space complexity is O(N), since `genealogy` may carry all the nodes.
"""