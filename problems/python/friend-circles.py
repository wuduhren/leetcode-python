"""
For every person #[1]
We use `dfs()` to traverse all its network and mark all the visited people. #[2]
So if the someone is visited, this means that he/she is in other people's friend cicle already. #[3]
So If Bob is never visited, `circles` adds 1 to represent all the people in the new network. #[4]

Time Complexity is O(N^2), we at most travel every node in the 2D array.
Space Complexity is O(N).
"""
class Solution(object):
    def findCircleNum(self, M):
        def dfs(i):
            stack = [i]
            while stack and len(stack)>0:
                node = stack.pop()
                visited.add(node) #[2]
                for j in xrange(len(M)):
                    if M[node][j]==1 and j not in visited:
                        stack.append(j)

        circles = 0
        visited = set()
        for i in xrange(len(M)): #[1]
            if i in visited: continue #[3]
            dfs(i)
            circles+=1 #[4]

        return circles
"""
We use the `roots` to store every node's root.
So if at index 1 value is 5, means that node1's root is node5. #[1]

We use `find()` to find a node's root by finding the node's parent and parent's parnet... #[2]
Along the way, we also update all the node we encounter.
This technique is also called path compression.

So for every connection, we `union()`, making those two node and all of their parent point to the same root. #[3]
All the children under the root is in the same friend circle.

At last, we count how many unique root in `roots`. #[4]

When we `find()`, we only update all the node's parents until we reach the root. #[5]
We did not update the node's child.
That is why we need to `find()` every node again.
To make sure all nodes in the `roots` has the right value.

Time Complexity is O(N^2) for `find()` is really close to O(1) in average.
Space Complexity is O(N)
"""
class Solution(object):
    def findCircleNum(self, M):
        def find(x):
            if x != roots[x]:
                roots[x] = find(roots[x])
            return roots[x]

        def union(p1, p2): #[2]
            p1_root = find(p1)
            p2_root = find(p2)
            roots[p1_root] = p2_root

        roots = [i for i in xrange(len(M))] #[1]

        for p1 in xrange(len(M)):
            for p2 in xrange(len(M)):
                if M[p1][p2] == 1:
                    union(p1, p2) #[3]
        
        roots = [find(i) for i in roots] #[5]
        return len(set(roots)) #[4]


M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
s = Solution()
s.findCircleNum(M)



# 2020/8/12
class Solution(object):
    def findCircleNum(self, M):
        if not M or not M[0]: return 0
        count = 0
        visited = set()
        
        for student in xrange(len(M)):
            if student in visited: continue
            
            count += 1

            #dfs
            stack = [student]
            while stack:
                curr_student = stack.pop()
                if curr_student in visited: continue
                visited.add(curr_student)
                stack.extend([class_mate for class_mate, is_friend in enumerate(M[curr_student]) if is_friend])
                
        return count

"""
If you don't know, DFS, please figure it out then come back.

For every `student`, we use DFS to find all of his direct friends. And put them into `visited`.
Every time we perform a DFS means putting an entire friend circle into `visited`.

Time Complexity: O(N).
Space Complexity: O(N).
"""