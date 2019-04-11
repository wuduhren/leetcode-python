"""
As the desscription:
You cannot update some cells first and then use their updated values to update other cells.

If we wanted to change the state in place,
We need to set another number that can represent the state now and the next state
So we don't mess up our count.

So I use 
3 means alive now and going to die,
2 means dead now and going alive.

All the '%2' in the count_alive() is just a way to make it cleaner [0]
Avoiding bunch of if-else
Because 3%2==1 and 2%2==0

Time Complexity is O(MN)
Because we go through the whole board once [1]
Each time at a (i,j) we use O(1) to count its alive neighbor [2]
And go through the whole board another time to convert 3->0 and 2->1 [3]
O(MN*1+MN)~=O(MN)

Space Complexity is O(1)
Because we done it in place.

I learn this really nice and clean solution from @zhuyinghua1203
"""
class Solution(object):
    def gameOfLife(self, board):
        if board==None or len(board)==0 or len(board[0])==0: return board

        m = len(board)
        n = len(board[0])
        
        def count_alive(i, j):
            if i<0 or j<0 or i>=m or j>=n: return 0
            count = 0

            #bottom, top, right, left
            if i+1<m: count+=board[i+1][j]%2 #[0]
            if 0<=i-1: count+=board[i-1][j]%2
            if j+1<n: count+=board[i][j+1]%2
            if 0<=j-1: count+=board[i][j-1]%2

            #bottomright, topleft, bottomleft, topright
            if i+1<m and j+1<n: count+=board[i+1][j+1]%2
            if 0<=i-1 and 0<=j-1: count+=board[i-1][j-1]%2
            if i+1<m and 0<=j-1: count+=board[i+1][j-1]%2
            if 0<=i-1 and j+1<n: count+=board[i-1][j+1]%2

            return count

        for i in xrange(m): #[1]
            for j in xrange(n):
                count = count_alive(i, j) #[2]

                if board[i][j]==1:
                    if count<2 or count>3:
                        board[i][j] = 3
                elif board[i][j]==0:
                    if count==3:
                        board[i][j] = 2

        for i in xrange(m): #[3]
            for j in xrange(n):
                if board[i][j]==2:
                    board[i][j] = 1
                elif board[i][j]==3:
                    board[i][j] = 0

        return board
