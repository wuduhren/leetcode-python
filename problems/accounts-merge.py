from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        graph = defaultdict(list)
        merged = set()
        ans = []

        #[0]
        for data in accounts:
            emails = data[1:]
            for i, email in enumerate(emails):
                graph[email].extend(emails[:i])
                graph[email].extend(emails[i+1:])
        
        for data in accounts:
            name = data[0]
            visited = set()
            stack = [data[1]] #[2]

            if data[1] in merged: continue #[1]
            
            while stack:
                e = stack.pop()
                if e in visited: continue
                visited.add(e)
                stack.extend(graph[e])
            
            merged.update(visited)
            ans.append([name]+sorted(list(visited))) #[3]
        
        return ans

"""
Treat each email as a node.
Build an adjacency graph. [0]

For every account's data
First, lets check if the first email is already merged. [1]
If the first email is already merged to other groups, then other emails will be in another group as well.
So don't need to check.

Second, do a DFS starting from the first email. Put all the connected nodes into visited. [2]
And append the sorted(visited) to the ans with name. [3]

Let N be the total number of emails. M be the total number of final groups.
Build the graph takes O(N).
For each final groups, we make a DFS to all nodes, taking O(MN).
Sort the group takes O((N/M)*Log(N/M)) -> O((N/M)*(logN-LogM))
Time: O(MN)
Space: O(N)
"""