class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        vector<vector<long long>> cost_graph(26, vector<long long>(26, INT_MAX));

        for (int i = 0; i < original.size(); i++) {
            int u = (int)original[i] - (int)'a';
            int v = (int)changed[i] - (int)'a';
            cost_graph[u][v] = min(cost_graph[u][v], (long long)cost[i]);
        }

        for (int k = 0; k < 26; k++) {
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < 26; j++) {
                    cost_graph[i][j] = min(cost_graph[i][j], cost_graph[i][k] + cost_graph[k][j]);
                }
            }
        }

        long long total_cost = 0;
        for (int i = 0; i < source.length(); i++) {
            if (source[i] == target[i]) {
                continue;
            }

            int r = (int)source[i] - (int)'a';
            int c = (int)target[i] - (int)'a';

            if (cost_graph[r][c] == (long long)INT_MAX) {
                return -1;
            }

            total_cost += cost_graph[r][c];
        }

        return total_cost;
    }
};