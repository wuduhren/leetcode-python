class Solution(object):
    def distributeCoins(self, root):
        def count_moves(node):
            if not node: return 0
            l, r = count_moves(node.left), count_moves(node.right)
            self.moves += abs(l)+abs(r)
            return node.val-1+l+r

        self.moves = 0
        count_moves(root)
        return self.moves

"""
If the leaf of a tree has 0 coins (an excess of -1 from what it needs), then we should push a coin from its parent onto the leaf.
If it has say, 4 coins (an excess of 3), then we should push 3 coins off the leaf.
In total, the number of moves from that leaf to or from its parent is excess = Math.abs(num_coins - 1).
Afterwards, we never have to consider this leaf again in the rest of our calculation.

`count_moves(node)` count the node.left and node.right moves and return the excess number of coins in the subtree at or below this node.
"""