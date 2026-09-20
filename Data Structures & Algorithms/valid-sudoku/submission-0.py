
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                # Check if it exists in any of the corresponding sets
                if (val in row[i]) or (val in col[j]) or (val in box[(i//3, j//3)]):
                    return False
                
                row[i].add(val)
                col[j].add(val)
                box[(i//3, j//3)].add(val)
                
        return True