from collections import deque
class Codec:
    def serialize(self, root):
        if root==None: return ''
        s=''
        queue = deque([root])
        while queue:
            node = queue.popleft()
            s+=str(node.val)+','
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return s[:-1]
            
    def deserialize(self, data):
        if data==None or data=='': return None
        data = map(int, data.split(','))
        root = TreeNode(data[0])
        for i in xrange(1, len(data)):
            val = data[i]
            node = root
            while True:
            	if val==node.val:
            		print('Input Error')
                elif val>node.val:
                    if node.right==None:
                        node.right = TreeNode(val)
                        break
                    else:
                        node = node.right
                else:
                    if node.left==None:
                        node.left = TreeNode(val)
                        break
                    else:
                        node = node.left
        return root

#2020/7/13
from collections import deque
class Codec:

    def serialize(self, root):
        s = ''
        if not root: return s

        q = deque([root])
        while q:
            node = q.popleft()
            s += str(node.val)+','
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        return s[:-1]

    def deserialize(self, data):
        def insert(root, node):
            if node.val<=root.val:
                if not root.left:
                    root.left = node
                else:
                    insert(root.left, node)
            else:
                if not root.right:
                    root.right = node
                else:
                    insert(root.right, node)

        if not data: return None

        vals = [int(val) for val in data.split(',')]
        root = TreeNode(vals[0])
        for i in xrange(1, len(vals)):
            val = vals[i]
            insert(root, TreeNode(val))

        return root

"""
Perform BFS to traverse the whole tree.
After we add the entire level to the string, then we go to the next level.

By doing this, we can always convert the serialized tree back.
Because when you build the tree back.
The order doesn't matter as long as you insert each parent before child.

For serialize(), the time and space complexity is O(N).
Because we use BFS to trverse each node once and store its val in string.

For deserialize(), the time complexity is O(NlogN).
Because we for every node, we perform insert(), which takes O(LogN) on a BST.
The space complexity is O(LogN), because the recusion will be LogN level deep.
"""