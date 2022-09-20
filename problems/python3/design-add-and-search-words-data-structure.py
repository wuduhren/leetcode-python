class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node['$'] = {} #'.' means the end of the word

    def search(self, word: str) -> bool:
        def helper(node, i):
            if i==len(word): return '$' in node
                
            if word[i]=='.':
                for c in node:
                    if helper(node[c], i+1): return True
                return False
            else:
                if word[i] not in node: return False
                return helper(node[word[i]], i+1)
        return helper(self.root, 0)
            
        
        
        
        
    
    
    
    