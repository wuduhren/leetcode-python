"""
Here is what I learn from @awice and solution approach 3.

There are two cases: #[0]
if n is small enough for all tasks to run without idle the answer would be len(tasks)
if n is not small enough
it would be like the Figure 2 in https://leetcode.com/problems/task-scheduler/Figures/621_Task_Scheduler_new.PNG
the answer of the case2 is the number of total number of square in the Figure 2

in Figure 2, we can see
n (cooling interval) is 4
max_count is 4, max_count is the max number of each task that is going to be executed
t is 2, t is the number of task with max_count, which is 'A' and 'B', they both have to be executed 4 times

t is the left over of the last row in Figure 2 #[1]
max_count-1 is the height of the Figure 2 except last row #[2]
n+1 is the width of the Figure
so in case2 the answer is (max_count-1)*(n+1)+t

in case2 there would be no way that t is 0
if t is zero, that means the last row don't have idle
if the last row don't have idle, there would be no idle for all the rows
in that case, it is case1

the answer is not possible to be smaller then len(tasks)
if your case2 answer is smaller than len(tasks), it is wrong
the situation would be case1
that is why we take the max out of two cases #[3]
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        task_count = collections.Counter(tasks).values()
        max_count = max(task_count) #[2]
        t = task_count.count(max_count) #[1]
        return max(len(tasks), (max_count-1)*(n+1)+t) #[3]