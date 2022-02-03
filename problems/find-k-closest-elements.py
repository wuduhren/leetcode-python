class Solution(object):
    def findClosestElements(self, arr, K, X):
        def isCloserThan(n1, n2, x):
            return abs(x-n1)<abs(x-n2) or (abs(x-n1)==abs(x-n2) and n1<n2)
                
        output1 = []
        output2 = []
        
        r = bisect.bisect_left(arr, X)
        l = r-1
        
        while len(output1)+len(output2)<K:
            if r>=len(arr) or (l>=0 and isCloserThan(arr[l], arr[r], X)):
                output1.append(arr[l])
                l -= 1
            else:
                output2.append(arr[r])
                r += 1
        
        return output1[::-1]+output2
