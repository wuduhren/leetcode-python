class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def helper(row: int):
            if row==n:
                ans.append(convertFormat(queenCols))
                return
            
            for col in range(n):
                posDiag = row+col
                negDiag = row-col
                
                if col in colUsed or posDiag in posDiagUsed or negDiag in negDiagUsed: continue
                
                queenCols.append(col)
                colUsed.add(col)
                posDiagUsed.add(posDiag)
                negDiagUsed.add(negDiag)
                
                helper(row+1)
                
                queenCols.pop()
                colUsed.remove(col)
                posDiagUsed.remove(posDiag)
                negDiagUsed.remove(negDiag)
        
        def convertFormat(queenCols: List[int]) -> List[str]:
            output = []
            for col in queenCols:
                row = ''
                for i in range(n):
                    if i==col:
                        row += 'Q'
                    else:
                        row += '.'
                output.append(row)
            return output
            
        ans = []
        queenCols = []
        colUsed = set()
        posDiagUsed = set()
        negDiagUsed = set()
        
        helper(0)
        return ans