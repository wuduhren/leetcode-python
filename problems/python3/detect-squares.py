class DetectSquares:

    def __init__(self):
        self.store = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.store[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0
        
        for dx, dy in self.store:
            if abs(x-dx)!=abs(y-dy) or x==dx or y==dy: continue
            ans += self.store[(dx, dy)]*self.store[(dx, y)]*self.store[(x, dy)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)