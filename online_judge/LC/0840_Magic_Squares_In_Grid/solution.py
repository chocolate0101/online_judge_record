# solution 1
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        pattern = "61834927" * 2
        pattern_reverse = "61834927"[::-1] * 2
        ans = 0
        
        row_length = len(grid)
        col_length = len(grid[0])
        if row_length < 3 or col_length < 3:
            return 0

        for row in range(1, row_length - 1):
            for col in range(1, col_length - 1):
                if grid[row][col] != 5:
                    continue

                if grid[row-1][col-1] % 2 != 0:
                    continue
                
                surround = [str(grid[row-1][col-1]), str(grid[row-1][col]), 
                            str(grid[row-1][col+1]), str(grid[row][col+1]), 
                            str(grid[row+1][col+1]), str(grid[row+1][col]), 
                            str(grid[row+1][col-1]), str(grid[row][col-1])]

                surround_str = "".join(surround)

                if surround_str in pattern or surround_str in pattern_reverse:
                    ans += 1

        return ans

# solution 2
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_magic(r, c):
            vals = []
            for i in range(r, r+3):
                for j in range(c, c+3):
                    val = grid[i][j]
                    if val < 1 or val > 9: return False
                    vals.append(val)
            
            if len(set(vals)) != 9: return False
            
            if any(sum(grid[i][c:c+3]) != 15 for i in range(r, r+3)): return False
            if any(grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15 for j in range(c, c+3)): return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15: return False
            
            return True

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if grid[r+1][c+1] != 5:
                    continue
                if is_magic(r, c):
                    ans += 1
        return ans