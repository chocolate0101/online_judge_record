// solution 1
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int ans = 0;
        string pattern = "6183492761834927";
        string pattern_reverse = "7294381672943816";
        if (rows < 3 || cols < 3) {
            return 0;
        }

        for (int i = 1; i < rows - 1; i++) {
            for (int j = 1; j < cols - 1; j++) {
                if (grid[i][j] != 5) {
                    continue;
                }

                if (grid[i-1][j-1] % 2 != 0) {
                    continue;
                }

                string surround = "";
                surround += to_string(grid[i-1][j-1]);
                surround += to_string(grid[i-1][j]);
                surround += to_string(grid[i-1][j+1]);
                surround += to_string(grid[i][j+1]);
                surround += to_string(grid[i+1][j+1]);
                surround += to_string(grid[i+1][j]);
                surround += to_string(grid[i+1][j-1]);
                surround += to_string(grid[i][j-1]);

                if (pattern.find(surround) != string::npos || pattern_reverse.find(surround) != string::npos) {
                    ans++;
                }
            }
        }

        return ans;
    }
};

// solution 2
class Solution {
public:
    int numMagicSquaresInside(vector<vector<int>>& grid) {
        int R = grid.size();
        int C = grid[0].size();
        int ans = 0;

        for (int r = 0; r < R - 2; r++) {
            for (int c = 0; c < C - 2; c++) {
                if (isMagic(grid, r, c)) {
                    ans++;
                }
            }
        }
        return ans;
    }

private:
    bool isMagic(const vector<vector<int>>& grid, int r, int c) {
        if (grid[r+1][c+1] != 5) return false;
        int check_mask = 0;
        
        for (int i = r; i < r + 3; i++) {
            for (int j = c; j < c + 3; j++) {
                int val = grid[i][j];
                if (val < 1 || val > 9) return false;
                check_mask |= (1 << val);
            }
        }
        
        if (check_mask != 1022) return false;

        if (grid[r][c] + grid[r][c+1] + grid[r][c+2] != 15) return false;
        if (grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != 15) return false;
        if (grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15) return false;
        if (grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15) return false;

        if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15) return false;
        if (grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15) return false;

        return true;
    }
};