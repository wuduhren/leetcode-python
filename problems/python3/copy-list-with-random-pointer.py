"""
Time: O(N)
Space: O(1)

The easiest way would be maintaining a hash map for original node to the copy and the other way around. Then the rest is easy.
But this will take us O(N) of extra space.

Two pass solution with constant space.
First pass.
Create a copy of the original and store it inside "random".
The copy points to original's next and original's random.

Second pass.
Iterate through the nodes again.
This time we adjust the copy to point to the other copies.
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head
        
        node = head
        while node:
            copy = Node(node.val, node.next, node.random)
            node.random = copy
            node = node.next
        
        node = head
        while node:
            newNode = node.random
            if node.next: newNode.next = node.next.random
            if newNode.random: newNode.random = newNode.random.random
            node = node.next
        
        return head.random