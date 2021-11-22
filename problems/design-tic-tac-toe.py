"""
Time: O(1) for move().
Space: O(N).

We need to find a way to quikly check if the player wins after the move.
Checking the whole map row by row or column by column will take a lots of time.
What we do instead is to record the count of the placement for each row and colomn. Also the count of topright-bottomleft, topleft-bottomright placement.
So if any of the count adds up to n, the player wins.

self.records[0] stores player1's record.
self.records[1] stores player2's record.

For player1's record (self.records[0]),
record[0][row] stores the placement count of the row for player1.
record[1][col] stores the placement count of the col for player1.
record[2] stores the topright-bottomleft placement count for player1.
record[3] stores the topleft-bottomright placement count for player1.

For player2's record (self.records[1]),
record[0][row] stores the placement count of the row for player2.
record[1][col] stores the placement count of the col for player2.
record[2] stores the topright-bottomleft placement count for player2.
record[3] stores the topleft-bottomright placement count for player2.

Note that, when checkRecord() we only need to check the (row, col) we just placed.
So we can achieve O(1) in time.
"""
class TicTacToe(object):

    def __init__(self, n):
        self.records = [[[0]*n, [0]*n, 0, 0], [[0]*n, [0]*n, 0, 0]]
        self.n = n
        
        
    def move(self, row, col, player):
        record = self.records[player-1]
        record[0][row] += 1
        record[1][col] += 1
        if row==col: record[2] += 1
        if row+col==self.n-1: record[3] += 1

        if self.checkRecord(record, row, col): return player
            
        return 0
        
    def checkRecord(self, record, row, col):
        if record[0][row]==self.n: return True
        if record[1][col]==self.n: return True
        if record[2]==self.n: return True
        if record[3]==self.n: return True
        
        return False