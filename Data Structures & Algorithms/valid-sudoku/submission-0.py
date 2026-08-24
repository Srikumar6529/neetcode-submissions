class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = defaultdict(set)
        seenCol = defaultdict(set)
        seenGrid = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".": continue
                if (board[r][c] in seenRow[r] or
                    board[r][c] in seenCol[c] or
                    board[r][c] in seenGrid[(r//3,c//3)]):
                        return False
                seenRow[r].add(board[r][c])
                seenCol[c].add(board[r][c])
                seenGrid[(r//3,c//3)].add(board[r][c])
                
        return True