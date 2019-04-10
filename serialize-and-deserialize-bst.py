"""
perform BFS to traverse the whole tree
after we add the entire level to the string, then we go to the next level

by doing this, we can always convert the serialized tree back
because when you build the tree back
the order doesn't matter as long as you insert each parent before child
"""

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