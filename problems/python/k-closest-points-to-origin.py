class Solution(object):
    def kClosest(self, points, k):
        h = []
        
        for x, y in points:
            d = (x**2+y**2)**0.5
            if len(h)>=k and -h[0][0]>d:
                heapq.heappop(h)
                heapq.heappush(h, (-d, x, y))
            elif len(h)>=k and -h[0][0]<=d:
                pass
            else:
                heapq.heappush(h, (-d, x, y))
        
        return [(x, y) for _, x, y in h]


"""
1. Process `points` into `distances`.

2. Binary search the "distance". For every distance:
Split the elements in `distances` by distance
Put the ones smaller to smaller.
Put the ones larger to larger.
If len(smaller)<=k, then all the elements in the smaller must belong to the `ans`, do the same thing to the larger.
Else we ignore the larger and do the same thing to the smaller again.

Time: O(N)
The binary search range in average is N, N/2, N/4... = 2N
Space: O(N)
"""
class Solution(object):
    def kClosest(self, points, K):
        #[1]
        maxD = float('-inf')
        minD = float('inf')
        distances = []
        for x, y in points:
            distance = ((x**2+y**2)**0.5)
            distances.append((distance, x, y))
            maxD = max(maxD, distance)
            minD = min(minD, distance)
        
        #[2]
        ans = []
        smaller = []
        larger = []
        while K>0:
            #split distances into smaller and larger
            distance = (maxD+minD)/2
            for d, x, y in distances:
                if d<=distance:
                    smaller.append((d, x, y))
                else:
                    larger.append((d, x, y))
            
            if len(smaller)<=K:
                ans += smaller
                K -= len(smaller)
                distances = larger
                minD = distance
                larger = []
                smaller = []
            else:
                distances = smaller
                maxD = distance
                larger = []
                smaller = []
        
        return [(x, y) for _, x, y in ans]



"""
Quick Select
Time: O(N)
Space: O(N), can be optimize to O(1).
"""
class Solution(object):
    def kClosest(self, points, K):
		"""
		Start State:
		i = s #next element after "SSS"s
		t = s #unprocessed elements
		j = e #next element after "LLLL"s

		SSSPP?????LLL
		i t   j

		End State:
		SSSPPPPPLLLLL
		i   jt
		"""
        def quickSelect(distances, s, e, k):

            pivot = distances[(s+e)/2][0]
            i = s
            j = e
            t = s
            
            while t<=j:
                if pivot<distances[t][0]:
                    distances[t], distances[j] = distances[j], distances[t]
                    j -= 1
                elif pivot>distances[t][0]:
                    distances[t], distances[i] = distances[i], distances[t]
                    i += 1
                    t += 1
                else:
                    t += 1
            
            if i-s>=k:
                return quickSelect(distances, s, i, k)
            elif j-s+1>=k:
                return pivot
            else:
                return quickSelect(distances, t, e, k-(t-s))

        distances = []
        for x, y in points:
            distance = ((x**2+y**2)**0.5)
            distances.append((distance, x, y))
        
        kthSmallestDistance = quickSelect(distances, 0, len(distances)-1, K)
        
        ans = []
        for d, x, y in distances:
            if len(ans)==K: break
            if d<=kthSmallestDistance: ans.append((x, y))
        
        return ans