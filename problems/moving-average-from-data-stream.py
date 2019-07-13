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

