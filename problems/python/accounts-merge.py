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


#Union Find
class Solution(object):
    def accountsMerge(self, accounts):
        def find(x):
            p = parents[x]
            while p!=parents[p]:
                p = find(p)
            parents[x] = p
            return p
        
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1==p2: return
            parents[p2] = p1
        
        parents = {}
        mailToName = {}
        
        for account in accounts:
            name = account[0]
            root = account[1]
            if root not in parents: parents[root] = root
            root = find(root)
            mailToName[root] = name
            
            for i in xrange(2, len(account)):
                email = account[i]
                if email in parents:
                    union(parents[email], root)
                    root = find(root)
                parents[email] = root
        
        rootToMails = collections.defaultdict(list)
        for email in parents:
            rootToMails[find(email)].append(email)
        
        ans = []
        for root in rootToMails:
            name = mailToName[root]
            mails = rootToMails[root]
            ans.append([name]+sorted(mails))
        
        return ans

#DFS
class Solution(object):
    def accountsMerge(self, accounts):
        
        #build adjacency list
        adj = collections.defaultdict(list)
        for account in accounts:
            name = account[0]
            email0 = account[1]
            for i in xrange(2, len(account)):
                email = account[i]
                adj[email0].append(email)
                adj[email].append(email0)
        
        #iterate accounts and dfs each email group
        ans = []
        visited = set() #store all the visited email
        for account in accounts:
            name = account[0]
            email0 = account[1]
            if email0 in visited: continue
            
            #dfs
            group = set() #store the email group related to email0
            stack = [email0]
            while stack:
                email = stack.pop()
                if email in group or email in visited: continue
                group.add(email)
                visited.add(email)
                for nei in adj[email]:
                    stack.append(nei)
            
            ans.append([name]+sorted(list(group)))
        
        return ans
            