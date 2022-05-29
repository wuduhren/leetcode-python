"""
Time for insert() O(N), search() O(N), startsWith() O(N). N is the number of characters.
Space for insert() O(N), search() O(1), startsWith() O(1). N is the number of characters.

Use . to represent the end of a string.
"""
class Node(object):
    def __init__(self, char):
        self.char = char
        self.children = {}

class Trie(object):

    def __init__(self):
        self.period = '.'
        self.root = Node('')
        

    def insert(self, word):
        word = word + self.period
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        

    def search(self, word):
        word = word + self.period
        node = self.root
        
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True
        

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True