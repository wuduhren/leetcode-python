"""
Time: O(NLogN)
Space: O(N)

1. In the paidGroup, one of the worker will be paid by his minimum wage.
Otherwise, the cost can be lower. Let's call this person "captain".
"captain" is getting paid "wage".

2. People in the paidGroup will be paid according to quality.
So people in the paidGroup is getting paid (individual quality) * (captain's wage/quality)
The total cost will be (sum of the quality in the paidGroup) * (captain's wage/quality).
So given a captain, we want the quality in the paidGroup as low as possible to have minimum cost.

3. Declare a list of worker's info (ratio, quality, wage).
Sort the list. Sorting the list is important.
In the next step, we are going to iterate over the workers and assume they are "captain".
This make sure that we can afford to pay worker already in the paidGroup larger than their minimum wage.

4. Iterate over the workers and assume they are "captain".
Also adding the worker to the paidGroup.
The paidGroup will at most have k people. With lowest quality. Using a max heap to maintain.
Also, tracking the total quality in the paidGroup (sumQ), so we can calculate the cost when `len(paidGroup)==k`.
Return the minimum cost.
"""
class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        cost = float('inf')
        
        workers = [(wage[i]/float(quality[i]), quality[i], wage[i]) for i in xrange(len(quality))]
        workers = sorted(workers)
        
        paidGroup = []
        sumQ = 0
        
        for r, q, w in workers:
            heapq.heappush(paidGroup, -q)
            sumQ += q
            
            if len(paidGroup)>k:
                sumQ -= -heapq.heappop(paidGroup)
            
            if len(paidGroup)==k:
                cost = min(cost, sumQ*r)
        
        return cost