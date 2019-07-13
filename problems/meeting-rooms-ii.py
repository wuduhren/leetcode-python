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







