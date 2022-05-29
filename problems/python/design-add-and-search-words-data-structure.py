class Node(object):
    def __init__(self, char):
        self.char = char
        self.children = {}
        
class WordDictionary(object):

    def __init__(self):
        self.root = Node('')
        self.endSign = ';'

    def addWord(self, word):
        word = word + self.endSign
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(c)
            node = node.children[c]
        
    def search(self, word):
        word = word + self.endSign
        return self.searchFromNode(self.root, word)
    
    def searchFromNode(self, node, word):
        if not word: return True
        
        char = word[0]
        if char in node.children:
            return self.searchFromNode(node.children[char], word[1:])
        elif char=='.':
            for c in node.children:
                if self.searchFromNode(node.children[c], word[1:]):
                    return True
        return False
        