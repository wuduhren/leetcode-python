"""
In both solution, the `counter` counts how many of each num in nums, as `counter[num]`=`num's count`
The bottle neck is we need to get k nums which has largest count (in an efficient way).
And here is how `Bucket Sort` and `Heap` comes in.

* Bucket Sort can sort things really quick, the trade off is we need to use lots of space. 
Now, because we know that the max possible count of each `num` is the count of `nums`.
We can make an list (`bucket`), where index 0~`len(nums)`, representing the count.
Every index `i` stores a list. In the list, all `num`  has exactly i count.
Next we can iterate backward, from large index to small index (from higher count to lower count), until we got k element in the output.

* Heap. We use the counter to build a max heap. Then we pop out the num which has higher count.

Time space analysis.
* Bucket Sort. For time complexity, build the counter takes O(N), build the bucket also takes O(N).
Getting the k num which has the highest count also takes O(N). So time complexity, is O(N).
Space complexity is O(N). For buckets at most takes every element in `nums`.

* Heap. For time complexity, build the counter takes O(N), build the heap also takes O(N).
(Yeah, I know. Some People thinks `heapify` takes O(NLogN) but it actually takes O(N). But that is another story...)
Pop out from heap takes O(N) and we do that k times, kLogN.
So time complexity, is O(N+kLogN).
Space complexity is O(N).
"""


from collections import Counter, defaultdict
import heapq

# bucket sort
class Solution(object):
    def topKFrequent(self, nums, k):
        opt = []
        counter = collections.Counter(nums)
        bucket = collections.defaultdict(list)

        for num, count in counter.items():
            bucket[count].append(num)

        for i in reversed(xrange(len(nums)+1)):
            if i in bucket:
                opt.extend(bucket[i])
                if len(opt)>=k: break

        return opt[:k]

# heap
class Solution(object):
    def topKFrequent(self, nums, k):
        opt = []
        counter = collections.Counter(nums)

        heap = [(-count, num) for num, count in counter.items()]
        heapq.heapify(heap)
        
        while len(opt)<k:
            opt.append(heapq.heappop(heap)[1])

        return opt


"""
Time: O(N+KLogN).
Building numToCounts takes O(N).
Building heap takes O(N) (Yeah, I know. Some People thinks `heapify` takes O(NLogN) but it actually takes O(N). But that is another story...).
HeapPop takes O(LogN).

Space: O(N)

1. Form `[(-count1, num1), (-count2, num2)]`, in this case `h`.
Use "-count" its because heapq in python is min heap, so using negative value will make it pop out the most freq count.

2. Turn h into heap. (heapify)

3. HeapPop h for k times.
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        ans = []
        
        numToCounts = collections.Counter(nums)
        h = [(-numToCounts[num], num) for num in numToCounts]
        
        heapq.heapify(h)
        
        while k>0:
            _, num = heapq.heappop(h)
            ans.append(num)
            k -= 1
        
        return ans

"""
Bucket sort for counts.
Space/Time: O(N)
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        counter = collections.Counter(nums)
        count2Nums = [[] for _ in xrange(len(nums)+1)] #count2Nums[i] := elements with count i
        
        for num in counter:
            count2Nums[counter[num]].append(num)
        
        ans = []
        for i in xrange(len(count2Nums)-1, -1, -1):
            ans += count2Nums[i]
            if len(ans)>=k: break
        
        return ans


# Quick Select
class Solution(object):
    def topKFrequent(self, nums, K):
        def quickselect(A, s, e, K):
            i = s
            t = s
            j = e
            
            pivot = A[(s+e)/2][0]
            while t<=j:
                if A[t][0]<pivot:
                    A[t], A[i] = A[i], A[t]
                    i += 1
                    t += 1
                elif A[t][0]==pivot:
                    t += 1
                else:
                    A[t], A[j] = A[j], A[t]
                    j -=1
            
            if e-j>=K:
                return quickselect(A, j+1, e, K)
            elif e-(i-1)>=K:
                return pivot
            else:
                return quickselect(A, s, i-1, K-(e-i+1))
                
        ans = []
        counter = collections.Counter(nums)
        freqs = [(counter[num], num) for num in counter]
        
        KthLargestFreq = quickselect(freqs, 0, len(freqs)-1, K)
        
        for freq, num in freqs:
            if freq>=KthLargestFreq: ans.append(num)
                
        return ans