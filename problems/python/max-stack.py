#https://leetcode.com/problems/max-stack/

#peekMax() and popMax() are O(N)
#Else are O(1)
class MaxStack(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        self.stack.append(x)
        

    def pop(self):
        return self.stack.pop()
        
        
    def top(self):
        return self.stack[-1]
        

    def peekMax(self):
        return max(self.stack)
        

    def popMax(self):
        max_num = None
        max_index = None
        
        for i in range(len(self.stack)):
            num = self.stack[i]
            if num>=max_num:
                max_num = num
                max_index = i

        return self.stack.pop(max_index)