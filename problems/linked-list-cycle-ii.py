class Solution(object):
    def detectCycle(self, head):
        curr = head
        while curr:
            if hasattr(curr, 'visited') and curr.visited: return curr
            curr.visited = True
            curr = curr.next
        return None

class Solution(object):
    def detectCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited: return True
            visited.add(curr)
            curr = curr.next
        return False