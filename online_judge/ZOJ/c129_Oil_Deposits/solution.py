# link of the question: https://zerojudge.tw/ShowProblem?problemid=c129

def bfs(grid, row, column):
    if not ( 0 <= row < len(grid) and 0 <= column < len(grid[0]) ):
        return
    if grid[row][column] == "*":
        return
    grid[row][column] = "*"
    
    direction = [[-1, 0], [-1, -1], [-1, 1], [0, -1], [0, 1], [1, 0], [1, -1], [1, 1]]
    for row_direction, column_direction in direction:
        bfs(grid, row + row_direction, column + column_direction)
        
    

while True:
    grid_size = list(map(int, input().split()))
    grid = []
    if grid_size == [0, 0]:
        break
    
    for i in range(grid_size[0]):
        grid.append(list(input()))
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                count += 1
                bfs(grid, i, j)

    print(count)