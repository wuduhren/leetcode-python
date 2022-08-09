#"stack" is just a normal stack.
#"minStack" stores the min of the stack element in the same position.
#i.e. At the time stack[x] put in to the stack. minStack[x] is the min.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minStack.append(val if (not self.minStack or val<self.minStack[-1]) else self.minStack[-1])

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minStack[-1]