class Solution(object):
    def canVisitAllRooms(self, rooms):
        if not rooms: return True
        
        visited = set()
        stack = [0]

        while stack:
            key = stack.pop()
            if key in visited: continue
            visited.add(key)
            stack.extend(rooms[key])

        return len(rooms)==len(visited)

"""
Time: O(N).
Space: O(N).
N is the number of rooms.
"""