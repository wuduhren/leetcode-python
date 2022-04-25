"""
`l` is the minimum possible ans.
`h` is the lowest value that we are sure that koko is able to finish all.
Since koko have to rest for the entire K even if he finish that pile already.
The H cannot be lowwer than `len(piles)`.
So we are sure that koko is able to finish all the piles in `max(piles)` of speed.

Now, we need to make logical guess between `l` and `h` by binary search.
If `m` (`(l+h)/2`) is able to finish all the piles in `H`, we lowwer the `h` to `m`.
If `m` is not able to finish, we raise the `l` to `m+1`.
We keep on adjust `l` and `r` until `l` is equal to `r`.
"""
class Solution(object):
    def minEatingSpeed(self, piles, H):
        def canEatAll(time):
            return sum((p+time-1)/time for p in piles) <= H
            # time_required = 0
            # for count in piles:
            #     time_required += math.ceil(count/float(time))
            # return time_required<=H

        l = 1
        h = max(piles)

        while l<h:
            m = (l+h)/2
            if canEatAll(m):
                h = m
            else:
                l = m+1
        return l


#2020/7/23
class Solution(object):
    def minEatingSpeed(self, piles, H):
        if not piles: return 0
        
        l = 1
        r = max(piles) #[0]
        
        while l<r:
            K = (l+r)/2 #[1]
            
            #time Koko needs to eat all bananas
            t = sum([-(-banana_count//K) for banana_count in piles]) #-(-a//b) means ceil(a/b)
            
            if t>H:
                #K cannot be the answer.
                #next round we don't need to put K in l~r.
                l = K+1
            else:
                #K might ot might not be the answer.
                #next round we still need to put K in l~r.
                r = K

        return l #[2]

"""
This is a binary search problem.
If you do not understand binary search yet, please study it first.

[0]
Lets define the possible range, `l` and `r`, of our answer, the minimum integer `K` such that Koko can eat all the bananas within `H` hours.
The best scenario is that Koko can eat the whole pile at once.
So `K` must be between 1 ~ `max(piles)`. `l = 1`, `r = max(piles)`.

[1]
For every iteration, we try a `K` and adjust `l` and `r`.
Note that, even if `t<=H`, we still need to see if there are any smaller `K`.

[2]
So the boundary of our answer, `l` and `r`, will collides together (`l==r`) and jump out of the loop.

Time complexity: `O(NlogN)`. There will be `O(LogN)` iteration. For every iteration we need O(N) to calculate the `t`. `N` is the length of `piles`.
Space complexity is O(N). For calculating `t`.
"""