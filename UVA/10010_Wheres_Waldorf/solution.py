def dfs(row, col, index, row_direction, col_direction, length):
    if index == length:
        return 1
    
    if not 0 <= row+row_direction < m or not 0 <= col+col_direction < n:
        return 0
    elif grid[row+row_direction][col+col_direction] == target[index]:
        index += 1
        return dfs(row+row_direction, col+col_direction, index, row_direction, col_direction, length)
    else:
        return 0



cases = int(input())
direction = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for case in range(cases):
    _ = input()
    m, n = map(int, input().split())

    grid = []
    for _ in range(m):
        tmp_str = input().lower()
        tmp_list = list(tmp_str)
        grid.append(tmp_list)

    target_cases = int(input())
    for _ in range(target_cases):
        target = input().lower()
        index = 0
        length = len(target)
        find = 0
        for i in range(m):
            for j in range(n):
                for k in direction:
                    if not 0 <= i+k[0] < m or not 0 <= j + k[1] < n:
                        continue

                    if grid[i][j] == target[index]:
                        find = dfs(i, j, index+1, k[0], k[1], length)

                    if find:
                        print(f"{i+1} {j+1}")
                        break

                if find:
                    break

            if find:
                break

    if case != cases-1:
        print()