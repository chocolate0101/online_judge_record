// solution 1 (BFS)
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        int max_sum_level = 1, max_sum = INT_MIN, cur_level = 0;
        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            cur_level++;
            int cur_sum = 0, q_length = q.size();
            for (int i = 0; i < q_length; i++) {
                TreeNode* cur_node = q.front();
                q.pop();
                cur_sum += cur_node->val;
                if (cur_node->left) {
                    q.push(cur_node->left);
                }
                
                if (cur_node->right) {
                    q.push(cur_node->right);
                }
            }

            if (cur_sum > max_sum) {
                max_sum = cur_sum;
                max_sum_level = cur_level;
            }
        }

        return max_sum_level;
    }
};

// solution 2 (DFS)
class Solution {
public:
    int maxLevelSum(TreeNode* root) {
        vector<int> level_sum;
        dfs(root, 1, level_sum);

        auto it = max_element(level_sum.begin(), level_sum.end());

        return distance(level_sum.begin(), it) + 1;

    }

    void dfs(TreeNode* node, int level, vector<int>& level_sum) {
        if (!node) {
            return ;
        }

        if (level_sum.size() < level) {
            level_sum.push_back(node->val);
        } else {
            level_sum[level-1] += node->val;
        }

        if (node->left) {
            dfs(node->left, level+1, level_sum);
        }

        if (node->right) {
            dfs(node->right, level+1, level_sum);
        }
    }
};