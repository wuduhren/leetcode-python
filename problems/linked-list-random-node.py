"""
Time: O(N) for __init__() and getRandom()
Space: O(1)
"""
class Solution(object):

    def __init__(self, head):
        self.count = 1
        self.curr = head
        
        while self.curr.next:
            self.curr = self.curr.next
            self.count += 1
        self.curr.next = head
        

    def getRandom(self):
        rand = randrange(self.count)
        while rand>0:
            rand -= 1
            self.curr = self.curr.next
        return self.curr.val