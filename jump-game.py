"""
Let's reverse engineer the process.
Imagine you are standing at the last index i
index i-1 will need the value>=1 to go to i (step_need=1)
index i-2 will need the value>=2 to go to i (step_need=2)
...

At a certain index x, the value>=step_need
This means that, from x, we can go to i no problem.
Now we are standing at x and reset step_need to 0.
See if we can repeat the process until we reach the first index.
"""
class Solution(object):
    def canJump(self, nums):
        step_need = 0
        for num in reversed(nums[:-1]):
            step_need+=1
            if num>=step_need:
                step_need = 0
        return step_need==0