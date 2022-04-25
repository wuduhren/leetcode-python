"""
Time: O(N). N is the number of char in string s. See below explanation.
Space: O(1)

The main idea is to add k different char to the ans every time.
The char with higher count will be used first.
So there will be more different kind of char left and will not be too close to each other.

To do this, we need a counter to track count of each char. [0]
And a heap so we can get the char with highest count fast (LogH). [0]
For each time, add k different char to the ans. [1]
Char with count>0 will be put back to h. [2]

If heap is drained before we add k element to the ans. It is not possible to form ans. Return emptry string. [3]

Time complexity:
Contruct counter takes O(N).
Contruct the heap (heapify) takes O(H), H is the number of element in the heap.
In the while loop, each char in s will be pop once. O(NLogH).
Since the problem said that the string will only have lower case letters. So H will at most be 26.
So O(N+H+NlogH) ~= O(N+26+NLog26) ~= O(N)
"""
class Solution(object):
    def rearrangeString(self, s, k):
        if k==0: return s
        ans = ''
        
		#[0]
        counter = collections.Counter(s)
        h = [(-counter[c], c) for c in counter]
        heapq.heapify(h)
        
        while h:
            l = []
            for i in xrange(k):
                _, c = heapq.heappop(h)
                ans += c
                counter[c] -= 1
                if counter[c]!=0: l.append((-counter[c], c)) #[2]
                
                if len(ans)==len(s): return ans
                if not h and i!=k-1: return '' #[3]
            
            for e in l: heapq.heappush(h, e)
        
        return ans #this line should never be executed