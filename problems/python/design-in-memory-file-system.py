"""
self.dirs is a nested hashmap to store the file structure.
self.files is a hashmap, mainly used to determine if the path is a "file", also used to store the content of the file.

Time: 
ls O(K)
mkdir O(K)
addContentToFile O(K)
readContentFromFile O(1)
K is the path count, for example /a/b/c/d, K=4.

Space:
O(N), N is the dir counts.
"""
class FileSystem(object):

    def __init__(self):
        self.files = {}
        self.dirs = {}

    def ls(self, path):
        if path in self.files:
            return [path.split('/')[-1]]
        else:
            if path=='/': return sorted(self.dirs.keys())
            curr = self.dirs
            for d in path.split('/')[1:]:
                curr = curr[d]
            return sorted(curr.keys())
        
    def mkdir(self, path):
        curr = self.dirs
        for d in path.split('/')[1:]:
            if d not in curr:
                curr[d] = {}
            curr = curr[d]
        
    def addContentToFile(self, filePath, content):
        if filePath not in self.files:
            self.mkdir(filePath)
            self.files[filePath] = content
        else:
            self.files[filePath] += content
            
    def readContentFromFile(self, filePath):
        return self.files[filePath]