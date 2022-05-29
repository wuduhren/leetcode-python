"""
[0] priceToTime tracks price to timestamps, but since for each timestamp the price might be overridden, the price in priceToTime might not be exsit. So we need to check if the price still have any valid timestamps.
[1] SortedDict is a BST like structure.

Time: O(LogN)
Space: O(N)
"""
from sortedcontainers import SortedDict #[1]

class StockPrice(object):

    def __init__(self):
        self.timeToPrice = SortedDict() #time will be sorted
        self.priceToTime = SortedDict() #the price will be sorted
        

    def update(self, timestamp, price):
        if timestamp in self.timeToPrice:
            prevPrice = self.timeToPrice[timestamp]
            self.priceToTime[prevPrice].remove(timestamp)
            if len(self.priceToTime[prevPrice])==0: self.priceToTime.pop(prevPrice) #[0]
        
        if price not in self.priceToTime: self.priceToTime[price] = set() #initialized
        self.priceToTime[price].add(timestamp)
        self.timeToPrice[timestamp] = price
            

    def current(self):
        return self.timeToPrice.peekitem(-1)[1]
        

    def maximum(self):
        return self.priceToTime.peekitem(-1)[0]
        

    def minimum(self):
        return self.priceToTime.peekitem(0)[0]