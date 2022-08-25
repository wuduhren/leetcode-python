class MedianFinder:

    def __init__(self):
        self.large = [] #store nums larger or equal to the median
        self.small = [] #store nums samaller to the median

    def addNum(self, num: int) -> None:
        if not self.large and not self.small:
            heapq.heappush(self.large, num)
        elif num>=self.findMedian():
            heapq.heappush(self.large, num)
            self.balance()
        else:
            heapq.heappush(self.small, -num)
            self.balance()
    
    def balance(self) -> None:
        #make the length of two heaps as even as posible
        if len(self.large)>len(self.small)+1:
            num = heapq.heappop(self.large)
            heapq.heappush(self.small, -num)
        
        if len(self.small)>len(self.large):
            num = -heapq.heappop(self.small)
            heapq.heappush(self.large, num)
    

    def findMedian(self) -> float:
        if (len(self.large)+len(self.small))%2==0:
            return (self.large[0]-self.small[0])/2
        else:
            return self.large[0]