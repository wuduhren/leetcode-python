class SparseVector:
    def __init__(self, nums):
        self.indices = set()
        self.values = {}
        
        for i, n in enumerate(nums):
            if n!=0:
                self.indices.add(i)
                self.values[i] = n
                
    def dotProduct(self, vec):
        products = 0
        indices = self.indices.intersection(vec.indices)
        for i in indices:
            products += self.values[i]*vec.values[i]
        return products