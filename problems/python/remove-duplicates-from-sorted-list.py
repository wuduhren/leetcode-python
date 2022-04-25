"""
The key is to use a set to remember if we seen the node or not.
Next, think about how we are going to *remove* the duplicate node?
The answer is to simply link the previous node to the next node.
So we need to keep a pointer `prev` on the previous node as we iterate the linked list.

So, the solution.
Create a set `seen`. #[1]
Point pointer `prev` on the first node. `cuur` on the second.
Now we iterate trough the linked list.
    * For every node, we add its value to `seen`. Move `prev` and `curr` forward. #[2]
    * If we seen the node, we *remove* the `curr` node. Then move the curr forward. #[3]
Return the `head`
"""
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head

        prev = head
        curr = head.next
        seen = set() #[1]

        seen.add(prev.val)
        while curr:
            if curr.val not in seen: #[2]
                seen.add(curr.val)
                curr = curr.next
                prev = prev.next
            else: #[3]
                prev.next = curr.next #remove
                curr = curr.next
        return head
