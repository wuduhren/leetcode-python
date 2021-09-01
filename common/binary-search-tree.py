class Node(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val


class BinarySearchTree(object):
	def __init__(self, val):
		self.root = Node(val)

	def insert(self, val):
		def helper(node, val):
			if val>node.val:
				if node.right:
					helper(node.right, val)
				else:
					node.right = Node(val)
			elif val<node.val:
				if node.left:
					helper(node.left, val)
				else:
					node.left = Node(val)
		helper(self.root, val)
		# self.printTree()

	def search(self, val):
		def helper(node, val):
			if node==None:
				return False
			elif val==node.val:
				return True
			elif val>node.val:
				return helper(node.right, val)
			elif val<node.val:
				return helper(node.left, val)

		print helper(self.root, val)
		# self.printTree()

	def inOrderPrint(self):
		def helper(node):
			if node.left: helper(node.left)
			print node.val
			if node.right: helper(node.right)
		helper(self.root)
		
	def preOrderPrint(self):
		def helper(node):
			print node.val
			if node.left: helper(node.left)
			if node.right: helper(node.right)
		helper(self.root)

	def postOrderPrint(self):
		def helper(node):
			if node.left: helper(node.left)
			if node.right: helper(node.right)
			print node.val
		helper(self.root)

tree = BinarySearchTree(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.insert(5)
tree.insert(7)

tree.inOrderPrint()
print '====='
tree.preOrderPrint()
print '====='
tree.postOrderPrint()
print '====='

tree.search(3)
tree.search(10)

















	

