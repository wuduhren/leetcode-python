#Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = collections.defaultdict(list)
        counter = collections.Counter(nums)
        ans = []
        
        for num in counter:
            bucket[counter[num]].append(num)
        
        tempCount = len(nums)
        while len(ans)<k:
            ans.extend(bucket[tempCount])
            tempCount -= 1
        
        return ans

#QuickSelect
class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        def quickSelect(freqs, s, e, K):
            i = s
            t = s
            j = e
            pivot = freqs[(s+e)//2][1]
            
            while t<=j:
                if freqs[t][1]<pivot:
                    freqs[i], freqs[t] = freqs[t], freqs[i]
                    i += 1
                    t +=1
                elif freqs[t][1]>pivot:
                    freqs[j], freqs[t] = freqs[t], freqs[j]
                    j -= 1
                else:
                    t += 1
            if e-j>=K:
                return quickSelect(freqs, j+1, e, K)
            elif e-(i-1)>=K:
                return pivot
            else:
                return quickSelect(freqs, s, i-1, K-(e-i+1))
                
        counts = collections.Counter(nums)
        freqs = [(num, counts[num]) for num in counts]
        ans = []
        
        KthLargestFreq = quickSelect(freqs, 0, len(freqs)-1, K)
        
        for num, freq in freqs:
            if freq>=KthLargestFreq:
                ans.append(num)
        return ans