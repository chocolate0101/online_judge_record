#include <bits/stdc++.h>
using namespace std;

int dfs(int row, int col, const int m, const int n, int index, 
    const int row_direction, const int col_direction, const int length, vector<vector<int>>& grid, string& target) {
    if (index == length) {
        return 1;
    }

    if (row+row_direction < 0 || row+row_direction >= m) {
        return 0;
    } else if (col+col_direction < 0 || col+col_direction >= n) {
        return 0;
    } else if (grid[row+row_direction][col+col_direction] == target[index]) {
        index += 1;
        return dfs(row+row_direction, col+col_direction, m, n, index, row_direction, col_direction, length, grid, target);
    } else {
        return 0;
    }
}

int main() {
    long long cases;
    cin >> cases;

    vector<pair<int, int>> direction = {
        {-1, -1}, {-1, 0}, {-1, 1},
        {0, -1}, {0, 1},
        {1, -1}, {1, 0}, {1, 1},
    };

    for (int i = 0; i < cases; i++) {
        string line;
        getline(cin, line);
        
        int m, n;
        cin >> m >> n;

        vector<vector<int>> grid(m);
        string tmp_str;
        for (int j = 0; j < m; j++) {
            cin >> tmp_str;
            for (auto& ch: tmp_str) {
                if (ch >= 'A' && ch <= 'Z') {
                    ch += 32;
                    grid[j].push_back(ch);
                } else {
                    grid[j].push_back(ch);
                }
            }
        }

        long long target_cases;
        cin >> target_cases;

        for (int j = 0; j < target_cases; j++) {
            string target;
            int index = 0;
            int target_length;
            cin >> target;
            for (auto& ch: target) {
                if (ch >= 'A' && ch <= 'Z') {
                    ch += 32;
                }
            }
            target_length = target.length();
            
            bool find = 0;
            for (int k = 0; k < m; k++) {
                for (int l = 0; l < n; l++) {
                    if (grid[k][l] == target[index]) {
                        if (target_length == 1) {
                            find = 1;
                            cout << k+1 << " " << l+1 << endl;
                            break;
                        } else {
                            for (int x = 0; x < direction.size(); x++) {
                                find = dfs(k, l, m, n, index+1, direction[x].first, direction[x].second, target_length, grid, target);
                                if (find) {
                                    cout << k+1 << " " << l+1 << endl;
                                    break;
                                }
                            }
                        }
                    }
                    
                    if (find) {
                        break;
                    }
                }
                
                if (find) {
                    break;
                }
            }
        }

        if (i != cases-1) {
            cout << endl;
        }
    }

    return 0;
}