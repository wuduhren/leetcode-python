#Flag
#Use a flag that stores on the nodes to know if we visited or not.
#time: O(N).
#space: O(N), for each node we use O(1) and there are N nodes.
class Solution(object):
    def detectCycle(self, head):
        curr = head
        while curr:
            if hasattr(curr, 'visited') and curr.visited: return curr
            curr.visited = True
            curr = curr.next
        return None

#HashSet
#Use a hash-set to store the visited nodes
#time: O(N).
#space: O(N).
class Solution(object):
    def detectCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited: return curr
            visited.add(curr)
            curr = curr.next
        return None