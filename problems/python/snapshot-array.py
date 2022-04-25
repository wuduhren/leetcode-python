class SnapshotArray(object):

    def __init__(self, length):
        self.data = [[(-1, 0)] for _ in xrange(length)]
        self.snapId = 0
        
        
    def set(self, index, val):
        self.data[index].append((self.snapId, val))
        
        
    def snap(self):
        self.snapId += 1
        return self.snapId - 1
            
        
    def get(self, index, snapId):
        j = bisect.bisect_right(self.data[index], (snapId, float('inf'))) - 1
        return self.data[index][j][1]