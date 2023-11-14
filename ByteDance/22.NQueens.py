class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        d, boards = set(), []

        def backtracking(row, leaft, board):
            if not leaft:
                boards.append([''.join(row )for row in board])
                return

            line = ['.' for _ in range(n)]
            for col in range(n):
                colKey = f'col_{col}'
                majorDiagKey = f'd1_{row-col}'
                subDiagKey = f'd2_{row+col}'
                local_d = set([colKey, majorDiagKey, subDiagKey])

                if local_d & d: continue 
                
                line[col] = 'Q'
                board.append(line)
                d.update(local_d)
                
                backtracking(row+1, leaft-1, board)
                line[col] = '.' 
                board.pop()  
                d.difference_update(local_d)            

        backtracking(0, n, [])
        
        return boards