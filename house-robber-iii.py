class Solution(object):
    def rob(self, root):
    	def set_max_value(node):
    		if node is None: return
    		print memo
    		if node.left is not None:
    			set_max_value(node.left)

    		if node.right is not None:
    			set_max_value(node.right)

    		memo[(node, True)] = node.val + get_max_value(node.left, False) + get_max_value(node.left, False)
    		memo[(node, False)] = get_max_value(node.left, True) + get_max_value(node.right, True)

    	def get_max_value(node, selected):
    		if node is None or (node, selected) not in memo:
    			print 'return 0'
    			return 0
			print 'return ', memo[(node, selected)]
			return memo[(node, selected)]

        memo = {}
        set_max_value(root)
        return max(get_max_value(root, True), get_max_value(root, False))