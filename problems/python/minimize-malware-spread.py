"""
Lets start from a node in the initial. DFS through the graph. [0]
When a node is infected, we paint it by color1.
After the DFS is done, we start from another node in the initial. DFS through the graph.
When a node is infected, we paint it by color2.
...

We don't paint the node that we already colored. [1]
The more node that are colored by an initial node the more affective it will minimize the malware. [2]
But if a color have two or more initial node, they won't make any difference if taken away. [3]
Because those node are still going to be infected by one another initial node.

So our goal here is to find the initial node that paint the most.
But did not paint other intial node.

I use 'color_data' to store the result [4]
{
    color1: [
        [intial nodes in this color],
        the number of node in this color
    ],
    color2: [
        ...
    ],
    color3: [
        ...
    ],
    ...
}

By 'color_data' I can easily see the things that I care about and calculate the answer
1. The intial nodes in this color
2. The number of node in this color

The time complexity is O(I*N), 
because we loop through the initial nodes.
And each node, it could potential travel all the nodes.
I is the initial nodes count, N is the nodes count.

Space complexity is O(N), because we use colored to keep track of all the nodes.
"""


class Solution(object):
    def minMalwareSpread(self, graph, initial):
        colored = set()
        initial_set = set(initial)
        color_data = {} #[4]
        color = 0
        
        def dfs(node, c):
            stack = [node]
            while stack:
                n = stack.pop()
                if n in colored: continue #[1]
                colored.add(n)

                if n in initial_set:
                    color_data[c][0].append(n)
                color_data[c][1]+=1

                for nb in xrange(len(graph)):
                    if graph[n][nb]==1:
                        stack.append(nb)
                
        # [0]
        for node in initial:
            if color not in color_data:
                color_data[color] = [[], 0]

            dfs(node, color)
            color+=1

        ans = min(initial)
        max_infected = float('-inf')
        for c in color_data.keys():
            if len(color_data[c][0])!=1: continue #[3]
            n = color_data[c][0][0]
            infected = color_data[c][1]

            if color_data[c][1]>max_infected: #[2]
                max_infected = infected
                ans = n
            elif infected==max_infected and n<ans:
                ans = n

        return ans

