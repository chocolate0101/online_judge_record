/*
Longest Squares

UVA 10908：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=1849#google_vignette
ZeroJudge e575：https://zerojudge.tw/ShowProblem?problemid=e575
GPE 考古：23551
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int num_test_case;
    cin >> num_test_case;

    int row, col, num_center_pos;
    for (int i = 0; i < num_test_case; i++) {
        // input the data
        cin >> row >> col >> num_center_pos;
    
        // input square
        vector<vector<char>> square(row, vector<char>(col));
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                cin >> square[i][j];
            }
        }

        // input center positions
        vector<pair<int, int>> center_pos(num_center_pos);
        for (int i = 0; i < num_center_pos; i++) {
            cin >> center_pos[i].first >> center_pos[i].second;
        }

        // check the biggest valid square
        vector<int> valid_square(num_center_pos, 1);
        for (int i = 0; i < num_center_pos; i++) {
            int x = center_pos[i].first;
            int y = center_pos[i].second;
            char character = square[x][y];
            
            for (int j = 1; ; j++) {
                int left = x - j;
                int right = x + j;
                int up = y - j;
                int down = y + j;
                int unvalid = 0;
                
                // out of range
                if (left < 0 || right >= row || up < 0 || down >= col) {
                    break;
                }

                // check horizontal character
                for (int k = up; k <= down; k++) {
                    if (character != square[left][k] || character != square[right][k]) {
                        unvalid = 1;
                        break;
                    }
                }
                
                if (unvalid) {
                    break;
                }

                // check vertical character
                for (int k = left; k <= right; k++) {
                    if (character != square[k][up] || character != square[k][down]) {
                        unvalid = 1;
                        break;
                    }
                }
                    
                if (unvalid) {
                    break;
                }
                
                // valid square found
                valid_square[i] += 2;
            }
        }

        cout << row << " " << col << " " << num_center_pos << endl;
        for (int i = 0; i < num_center_pos; i++) {
            cout << valid_square[i] << endl;
        }
    }

    return 0;
}