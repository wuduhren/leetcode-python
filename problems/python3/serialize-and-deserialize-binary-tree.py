class Codec:

    def serialize(self, root):
        if not root: return '#'
        return str(root.val)+','+self.serialize(root.left)+','+self.serialize(root.right)
        

    def deserialize(self, data):
        def helper():
            if data[self.i]=='#':
                self.i += 1
                return None
            
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = helper()
            node.right = helper()
            return node
        
        data = data.split(",")
        self.i = 0
        return helper()