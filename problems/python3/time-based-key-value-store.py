class TimeMap:

    def __init__(self):
        self.data = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        dataList = self.data[key]
        l = 0
        r = len(dataList)-1
        ans = ''
        
        while l<=r:
            m = l + int((r-l)/2)
            t = dataList[m][0]
            
            if t<timestamp:
                ans = dataList[m][1]
                l = m+1
            elif t>timestamp:
                r = m-1
            else:
                ans = dataList[m][1]
                break
        
        return ans