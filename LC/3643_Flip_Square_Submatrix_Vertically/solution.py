class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        left = x
        right = x + k - 1
        
        while (left <= right):
            for i in range(y, y+k):
                grid[left][i], grid[right][i] = grid[right][i], grid[left][i]
            
            left += 1
            right -= 1

        return grid