// solution 1
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] < 0) {
                    count++;
                }
            }
        }

        return count;
    }
};

// solution 2
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int m = grid.size();
        int n = grid[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] < 0) {
                    count += n - j;
                    break;
                }
            }
        }

        return count;
    }
};

// solution 3
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int n = grid[0].size();
        for (int i = 0; i < grid.size(); i++) {
            int left = 0;
            int right = n - 1;
            int mid;
            while (left <= right) {
                mid = left + (right - left) / 2;
                if (grid[i][mid] < 0) {
                    right = mid-1;
                } else {
                    left = mid+1;
                }
            }
            count += n - left;
        }
        return count;
    }
};

// solution 4
class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int count = 0;
        int m = grid.size() - 1;
        int column_size = grid[0].size();
        int n = 0;
        while (m >= 0 && n < column_size) {
            if (grid[m][n] >= 0) {
                n++;
            } else {
                count += column_size - n;
                m--;
            }
        }

        return count;
    }
};