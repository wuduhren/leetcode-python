# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if len(intervals)==0: return 0
        
        timeline = {}
        room_open = 0
        result = 0
        
        for inter in intervals:
            if inter.start not in timeline:
                timeline[inter.start] = [1, 0]
            else:
                timeline[inter.start][0]+=1
            if inter.end not in timeline:
                timeline[inter.end] = [0, 1]
            else:
                timeline[inter.end][1]+=1

        for time in timeline.keys().sort():
            room_open-=timeline[time][1]
            room_open+=timeline[time][0]
            result = max(result, room_open)

        return result



# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals: return 0

        free_rooms = []
        intervals.sort(key= lambda x: x.start)

        heapq.heappush(free_rooms, intervals[0].end)
        for i in intervals[1:]:
            if free_rooms[0]<=i.start:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i.end)

        return len(free_rooms)



#2021/8/12
"""
Time: O(NLogN)
Space: O(N)

1. Sort the intervals by the start time. So we can check the starttime in order.

2. Declare `h`. Imagine we store the room (endtime) we need in the `h`.
If a meeting comes up, first we will check if any room avaliable.
If so, take the room. (Remove the old endtime from `h` and add the current endtime)
If not, start a new room. (Add the current endtime)
Use heap so it will be convinient for us to get the earliest endtime at h[0] (most avaliable room).

3. At last, `h` will contain the rooms (endtimes) needed for all the intervals.
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        intervals.sort()
        h = [intervals[0][1]]
        
        for i in xrange(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if start>=h[0]:
                #the room at h[0] is avaliable
                heapq.heappop(h)
            heapq.heappush(h, end)
            
        return len(h)


"""
Time: O(NLogN)
Space: O(N)

e0, s0 is one of the previous meetings where the end time is the earliest (smallest).
"""
class Solution(object):
    def minMeetingRooms(self, intervals):
        if not intervals: return 0
        ans = 1
        h = []
        
        intervals.sort()
        heapq.heappush(h, (intervals[0][1], intervals[0][0]))
        
        for i in xrange(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            
            e0, s0 = h[0]
            
            if s>=e0: heapq.heappop(h)
            heapq.heappush(h, (e, s))
            ans = max(ans, len(h))
            
        return ans