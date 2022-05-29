"""
everytime we ping
we put the t in the queue

and check the leftmost(smallest) if it is in the range of 3000
if it is out of range, pop it, we don't need it anymore
bc it would definitely be out of range for the next ping
and bc the description says t is strictly increasing
keep do the same until the leftmost is in the range

now all the value in the queue is in the range
return the length of the queue
"""
from collections import deque
class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while len(self.q)>0 and self.q[0]<t-3000:
            self.q.popleft()
        
        return len(self.q)