#https://leetcode.com/problems/min-stack/
class MinStack(object):

    def __init__(self):
        self.s = []
        

    def push(self, x):
        self.s.append(x)
        

    def pop(self):
        self.s.pop(len(self.s)-1)
        

    def top(self):
        return self.s[len(self.s)-1]
        

    def getMin(self):
        return min(self.s)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()