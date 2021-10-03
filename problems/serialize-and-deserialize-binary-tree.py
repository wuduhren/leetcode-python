class Codec:

    def serialize(self, root):
        if not root: return ''
        q = collections.deque([root])
        s = ''
        while q:
            node = q.popleft()
            
            if node:
                s += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                s += '#'
            s += ','
        return s[:-1]
            
        
    def deserialize(self, data):
        if not data: return None
        
        data = data.split(',')
        root = TreeNode(data[0])
        q = collections.deque([root])
        i = 1
        
        while q and i<len(data):
            node = q.popleft()
            
            if data[i]!='#':
                node.left = TreeNode(data[i])
                q.append(node.left)
            i+=1
            
            if i>=len(data): continue
            if data[i]!='#':
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
            
        return root