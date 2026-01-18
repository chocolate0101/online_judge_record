/*
Error Correction

UVA 541：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=482
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    while(cin >> n) {
        if (n == 0) break;

        // input the matrix
        vector<vector<int>> matrix(n, vector<int>(n));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        // calculate the row sums
        vector<int> row_sum(n);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sum += matrix[i][j];
            }
            row_sum[i] = sum;
            sum = 0;
        }

        // calculate the column sums
        vector<int> column_sum(n);
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                sum += matrix[i][j];
            }
            column_sum[j] = sum;
            sum = 0;
        }
        
        // calculate the number of odd row and column and its position
        int row_odd= 0, col_odd = 0;
        vector<int> row_index;
        vector<int> col_index;
        for(int i = 0; i < n; i++) {
            if (row_sum[i] % 2 != 0) {
                row_index.push_back(i);
                row_odd++;
            }
            if (column_sum[i] % 2 != 0) {
                col_index.push_back(i);
                col_odd++;
            }
        }

        // print answer
        if (row_odd == 0 && col_odd == 0) {
            cout << "OK\n";
        } else if (row_odd == 1 && col_odd == 1) {
            cout << "Change bit (" << row_index[0]+1 << "," << col_index[0]+1 <<")\n";
        } else {
            cout << "Corrupt\n";
        }

    }
    return 0;
}