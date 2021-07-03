"""
self.booked := booked times.
self.overlaps := overlaped times.

For each new book,
1. check if the new book overlaps with the times in self.overlaps, if so, return False.
2. check if the new book overlaps with the times in self.booked, if so, store the overlaped time in self.overlaps.
3. store the new book in self.booked.
"""
class MyCalendarTwo(object):

    def __init__(self):
        self.overlaps = []
        self.booked = []
        

    def book(self, start, end):
        for s, e in self.overlaps:
            if not (e<=start or end<=s):
                return False
        
        for s, e in self.booked:
            if not (e<=start or end<=s):
                self.overlaps.append((max(start, s), min(end, e)))
        
        self.booked.append((start, end))
        return True