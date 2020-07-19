"""
I learn the answer from @realisking, I couldn't come up with such elegant solution myself.

On every node we got two option, to rob or not to rob
* To rob this node, then we cannot rob our left and right child, so the max value would be the total of
    * value of this node
    * the max value from left child, when we not rob the left child
    * the max value from right child, when we not rob the right child
* Not to rob this node, means that we can either rob or not rob our left and right child, so the max value would be the total of
    * 0, because we choose not to rob this node
    * the max of `rob the left child` and `not rob the left child`
    * the max of `rob the right child` and `not rob the right child`

`get_max_value(node)` returns the `max value when we rob this node` and `max value when we not rob this node` on each node.
So we get the max from the two returns from `get_max_value(root)`

The time complexity is `O(LogN)`, because we keep calling `get_max_value()` until the very bottom of the tree.
The space complexity is `O(LogN)`, too. Even we only use `O(1)` of space on every `get_max_value()`
But we used `LogN` level of recursion. `N` is the number of houses.
"""
class Solution(object):
    def rob(self, root):
        def get_max_value(node):
            if node is None: return 0, 0
            left_rob, left_not_rob = get_max_value(node.left)
            right_rob, right_not_rob = get_max_value(node.right)

            rob = node.val+left_not_rob+right_not_rob
            not_rob = max(left_rob, left_not_rob)+max(right_rob, right_not_rob)

            return rob, not_rob

        return max(get_max_value(root))
        