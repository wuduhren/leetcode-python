#Two Pointers
#If the linked list has cycle, the fast pointer will eventually catch up.
#time: O(N).
#space: O(1).
class Solution(object):
    def hasCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow: return True
        return False

#Flag
#Use a flag that stores on the nodes to know if we visited or not.
#time: O(N).
#space: O(N), for each node we use O(1) and there are N nodes.
class Solution(object):
    def hasCycle(self, head):
        curr = head
        while curr:
            if hasattr(curr, 'visited') and curr.visited: return True
            curr.visited = True
            curr = curr.next
        return False

#HashSet
#Use a hash-set to store the visited nodes
#time: O(N).
#space: O(N).
class Solution(object):
    def hasCycle(self, head):
        visited = set()
        curr = head
        while curr:
            if curr in visited: return True
            visited.add(curr)
            curr = curr.next
        return False
        
