# solution 1
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    count += 1

        return count

# solution 2
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    count += n - j
                    break

        return count
    
# solution 3
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid[0])
        for i in range(len(grid)):
            left, right, mid = 0, n - 1, 0
            while left <= right:
                mid = (left + right) // 2
                if grid[i][mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            count += n - left

        return count
    
# solution 4
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        m = len(grid) - 1
        n = 0
        column_size = len(grid[0])
        while m >= 0 and n < column_size:
            if grid[m][n] >= 0:
                n += 1
            else:
                count += column_size - n
                m -= 1

        return count