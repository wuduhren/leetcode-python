from collections import Counter

class Solution(object):
    def pathSum(self, root, sum):
        def helper(node, sum_from_root, record):
            sum_from_root += node.val
            sum_to_p = sum_from_root-sum
            self.ans += record[sum_to_p]

            record[sum_from_root] += 1 #1
            if node.left:
                helper(node.left, sum_from_root, record)
            if node.right:
                helper(node.right, sum_from_root, record)
            record[sum_from_root] -= 1 #2
        
        self.ans = 0
        if not root: return self.ans
        record = Counter()
        record[0] = 1 #3
        helper(root, 0, record)
        return self.ans

"""
This answer is inspired by @gabbu
Some variable and function:
1. `self.ans` stores the number of paths that sum to a given value.
2. `helper()` will traverse the tree and increase `self.ans` along the way.
3. `sum_from_root` is the sum from the `node` to the `root`. Note that, there maybe multiple ways to get to a node.
4. `record` is the number of ways that paths sums up to a number. In short, `record[any_sum]` you get **number of ways to have any_sum**.

0.
`record` is the hardest part to understand, you need to see the main idea below first.
Imagine we are now at a node in the tree, N. The sum of the path from root to N (including `N.val`) is `sum_from_root`.
Imagine a predecessor of N, we call it P. The sum of the path root->P (including N.val) is `sum_to_p`. Given a node N, there maybe multiple or no P.
`sum_to_p + sum(P->N) == sum_from_root`, thus `sum(P->N) == sum_from_root - sum_to_p`
This problem we are looking for **the number of ways P->N, where `sum == sum(P->N)`** (where `sum == sum_from_root - sum_to_p`).
Thus, we are basically looking for the number of ways root->P, where `sum_to_p == sum_from_root - sum`.
So that is why we have `record`. We can find the number of ways root->P by record[sum_to_p] (record[sum_from_root - sum]).

1.
Maintain the `record`.

2.
Remove the case from the `record` after all the children are done calculating.
This prevent other node counts the irerlevant `record`.

Time complexity is O(N). Since we only traverse each node once.
Space complexity O(N). Since in the worst case, we might go N-level of recursion.
"""