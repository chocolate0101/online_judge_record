# solution 1 (BFS)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum_level = 0
        max_sum = -inf
        q = deque()
        q.append(root)
        cur_level = 1
        
        while q:
            cur_sum = 0
            for _ in range(len(q)):
                cur_node = q.popleft()
                cur_sum += cur_node.val
                if cur_node.left != None:
                    q.append(cur_node.left)
                if cur_node.right != None:
                    q.append(cur_node.right)

            if cur_sum > max_sum:
                max_sum_level = cur_level
                max_sum = cur_sum

            cur_level += 1
        
        return max_sum_level
    
# solution 2 (DFS)
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum = []
        
        def dfs(nodes, level):
            if len(level_sum) < level:
                level_sum.append(0)

            level_sum[level-1] += nodes.val
            if nodes.left:
                dfs(nodes.left, level+1)
            if nodes.right:
                dfs(nodes.right, level+1)

        dfs(root, 1)

        max_sum = max(level_sum)

        return level_sum.index(max_sum) + 1