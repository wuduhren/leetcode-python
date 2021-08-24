"""
Time: O(N) for addNum() and O(1) for findMedian(). Though we can find the indext to insert in O(LogN) but insert still takes O(N)
Space: O(N).
"""
class MedianFinder(object):

    def __init__(self):
        self.a = []

    def addNum(self, num):
        bisect.insort_left(self.a, num)
        
    def findMedian(self):
        i = len(self.a)/2
        return (self.a[i-1]+self.a[i])/2.0 if len(self.a)%2==0 else self.a[i]


"""
Time: O(LogN) for addNum() and O(1) for findMedian().
Space: O(N).
"""
class MedianFinder(object):

    def __init__(self):
        self.smaller = [] #max heap
        self.larger = [] #min heap
        
    def addNum(self, num):
        if not self.smaller or num<-self.smaller[0]:
            heapq.heappush(self.smaller, -num)
        else:
            heapq.heappush(self.larger, num)
        
        if len(self.smaller)-len(self.larger)>1:
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))
        elif len(self.larger)-len(self.smaller)>=1:
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))
            
    def findMedian(self):
        return -self.smaller[0] if (len(self.smaller)-len(self.larger))%2!=0 else (-self.smaller[0]+self.larger[0])/2.0