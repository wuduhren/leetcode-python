"""
First thing, you must understand that if sum(gas)>=sum(cost) there must be an answer. Guaranteed.
If we know there is an answer, we can simply test all the index.
If the currGas ever drops to below 0, it means that we need to switch a "start".

Time: O(N)
Space: O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost): return -1
        
        start = 0
        currGas = 0
        
        for i in range(len(gas)):
            currGas += gas[i]-cost[i]
            
            if currGas<0:
                currGas = 0
                start = i+1
        
        return start