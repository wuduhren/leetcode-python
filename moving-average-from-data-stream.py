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
I really take time to make the best solution, because I wanted to help people understand.
If you like my answer, a star on GitHub I will really appreciated.
https://github.com/wuduhren/leetcode-python
"""