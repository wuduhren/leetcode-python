class Node(object):
    def __init__(self, val):
        self.val = val
        self.key = None
        self.children = {}

class Solution(object):
    def deleteDuplicateFolder(self, paths):
        def setKey(node):
            node.key = ''
            for c in sorted(node.children.keys()): #need to be sorted. so when child structs are the same, we won't generate different key from different iteration order.
                setKey(node.children[c])
                node.key += node.children[c].val + '|' + node.children[c].key + '|' #generate a key for each node. only considering its children structure. (see the "identical" definition, it does not consider the val of the node itself.)
                
            keyCount[node.key] += 1
        
        def addPath(node, path):
            if node.children and keyCount[node.key]>1: return #leaf node does not apply to this rule
            ans.append(path+[node.val])
            for c in node.children:
                addPath(node.children[c], path+[node.val])
            
            
        ans = []
        root = Node('/')
        keyCount = collections.Counter()
        
        #build the tree
        for path in paths:
            node = root
            for c in path:
                if c not in node.children: node.children[c] = Node(c)
                node = node.children[c]
        
        #set all nodes key recursively
        setKey(root)

        #build ans
        for c in root.children:
            addPath(root.children[c], [])
        
        return ans