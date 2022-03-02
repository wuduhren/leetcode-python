"""
1. Generate positions. Storing the mapping between number to indices.
2. Iterate from left, for each n1, find the largest number larger than n1 (searching from 9, 8, 7 to n1+1).
3. Since we need to find the max output. There might be multiple the same number, we need to find the index of the rightest number.
4. Remove n1 when it is done. Because right of the n1 should not consider it anymore.
"""
class Solution(object):
    def maximumSwap(self, num):
        numList = [int(n) for n in str(num)]
        positions = collections.defaultdict(list)
        for i, n in enumerate(numList): positions[n].append(i) #[1]
        
        i = 0
        for i, n1 in enumerate(numList): #[2]
            n1 = numList[i]
            for n2 in xrange(9, n1, -1): 
                if n2 in positions and len(positions[n2])>0:
                    j = positions[n2][-1] #[3]
                    numList[i], numList[j] = numList[j], numList[i]
                    return int(''.join([str(n) for n in numList]))
            positions[n1].pop(0) #[4]
            
        return num