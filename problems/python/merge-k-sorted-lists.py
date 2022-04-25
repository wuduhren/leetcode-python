"""
Time: O(NLogK). Popping and pushing to a heap with K elements takes O(LogK). There are N nodes in total.
Space: O(1).

All k lists are already sorted.
Put all k nodes in the head to the min heap. Each time, pop the one out.
Since it is a min heap the node popping out will be the smallest node.
For each node, attach it to the last node and push node.next to the heap.

Note that, heapq are not able to sort ListNode, so we need to put tuple of node.val and node to the heap: `(node.val, node)`
So the heap will sort it by node.val.
"""
class Solution(object):
    def mergeKLists(self, lists):
        h = [(node.val, node) for node in lists if node]
        heapq.heapify(h)
        
        preHead = ListNode()
        curr = preHead
        
        while h:
            _, node = heapq.heappop(h)
            if node.next: heapq.heappush(h, (node.next.val, node.next))
            curr.next = node
            curr = curr.next
        
        return preHead.next