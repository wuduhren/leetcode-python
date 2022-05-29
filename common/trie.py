class Node(object):
	def __init__(self):
		self.children = {}
		self.isEnd = False

	def get(self, char):
		if char in self.children:
			return self.children[char]
		else:
			return None

	def set(self, char):
		if char in self.children:
			return self.children[char]
		else:
			self.children[char] = Node()
			return self.children[char]

	def remove(self, char):
		self.children.pop(char, None)
		return len(self.children)==0


class Trie(object):
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		curr = self.root
		for i in xrange(len(word)):
			c = word[i]
			node = curr.get(c)
			if node is None: node = curr.set(c)
			if i==len(word)-1: node.isEnd = True
			curr = node

	def search(self, word):
		curr = self.root
		for i in xrange(len(word)):
			c = word[i]
			node = curr.get(c)
			if node is None: return False
			if i==len(word)-1: return node.isEnd
			curr = node

	def remove(self, word):
		curr = self.root
		stack = []
		for i in xrange(len(word)):
			c = word[i]
			node = curr.get(c)

			#the word does not exist
			if node is None: return

			stack.append((curr, c))
			curr = node

		#if the last node has other link
		#just set isEnd to False
		if len(curr.children)>0:
			curr.isEnd = False
			return

		while stack and len(stack)>0:
			node, c = stack.pop()
			emptyAfterRemove = node.remove(c)
			if not emptyAfterRemove: break


trie = Trie()
trie.insert('abc')
trie.insert('abgl')
trie.insert('cdf')
trie.insert('abcd')
trie.insert('lmn')
print trie.search('abc')
print trie.search('abcd')

trie.remove('abc')
print trie.search('abc')
trie.remove('abgl')
print trie.search('abgl')
trie.remove('abcd')
print trie.search('abcd')


