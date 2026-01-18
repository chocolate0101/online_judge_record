class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node.left:
                left_subtree_sum = dfs(node.left)
            else:
                left_subtree_sum = 0
            if node.right:
                right_subtree_sum = dfs(node.right)
            else:
                right_subtree_sum = 0

            node.val += left_subtree_sum + right_subtree_sum

            return node.val

        total = dfs(root)
        q = deque()
        q.append(root)
        ans = -inf

        while q:
            node = q.popleft()
            if not node:
                continue

            cur_product = (total - node.val) * node.val
            ans = max(ans, cur_product)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return int(ans % (1e9 + 7))