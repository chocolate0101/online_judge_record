# link of the question
# 尚未提交，因為那天沒搞懂

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                is_visit = [ [ 0 for _ in range(len(heights[0])) ] for i in range(len(heights))]
                pacific, atlantic = dfs(heights, is_visit, i, j)
                if pacific == 1 and atlantic == 1:
                    ans.append([i, j])
        return ans

def dfs(heights, is_visit, row_position, col_position):
    can_reach_pacific = 0
    can_reach_atlantic = 0

    if is_visit[row_position][col_position] == 1:
        return 0 , 0
    
    is_visit[row_position][col_position] = 1
    
    if row_position == 0 or col_position == 0:
        can_reach_pacific = 1
    
    if row_position == len(heights)-1 or col_position == len(heights[0])-1:
        can_reach_atlantic = 1

    if row_position+1 < len(heights) and heights[row_position][col_position] >= heights[row_position+1][col_position]:
        p, a = dfs(heights, is_visit, row_position+1, col_position)
        can_reach_pacific = can_reach_pacific or p
        can_reach_atlantic = can_reach_atlantic or a
    if col_position+1 < len(heights[0]) and heights[row_position][col_position] >= heights[row_position][col_position+1]:
        p, a = dfs(heights, is_visit, row_position, col_position+1)
        can_reach_pacific = can_reach_pacific or p
        can_reach_atlantic = can_reach_atlantic or a
    if row_position-1 >= 0 and heights[row_position][col_position] >= heights[row_position-1][col_position]:
        p, a = dfs(heights, is_visit, row_position-1, col_position)
        can_reach_pacific = can_reach_pacific or p
        can_reach_atlantic = can_reach_atlantic or a
    if col_position-1 >= 0 and heights[row_position][col_position] >= heights[row_position][col_position-1]:
        p, a = dfs(heights, is_visit, row_position, col_position-1)
        can_reach_pacific = can_reach_pacific or p
        can_reach_atlantic = can_reach_atlantic or a

    return can_reach_pacific, can_reach_atlantic