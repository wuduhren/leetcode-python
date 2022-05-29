class MovingAverage(object):

    def __init__(self, size):
        self.queue = collections.deque()
        self.size = size
        self.sum = 0
        
    def next(self, val):
        self.queue.append(val)
        
        if len(self.queue)>self.size:
            self.sum = self.sum+val-self.queue.popleft()
        else:
            self.sum = self.sum+val
            
        return self.sum/float(len(self.queue))

"""
Time: O(1)
Space: O(Size)
"""
class MovingAverage(object):

    def __init__(self, size):
        self.size = size
        self.q = collections.deque()
        self.sum = 0
        

    def next(self, val):
        if len(self.q)>=self.size:
            self.sum -= self.q.popleft()
        
        self.sum += val
        self.q.append(val)
        return float(self.sum)/len(self.q)