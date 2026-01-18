/*
Rank the language

UVA 10336：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1277
ZeroJudge d365：https://zerojudge.tw/ShowProblem?problemid=d365
GPE 考古：11006
*/

#include <bits/stdc++.h>
using namespace std;

void dfs(int row, int col, vector<vector<char>>& state_matrix, vector<vector<bool>>& visited, const char current_language) {
    if (row < 0 || row >= state_matrix.size() || col < 0 || col >= state_matrix[0].size() || visited[row][col] || state_matrix[row][col] != current_language) {
        return;
    }

    visited[row][col] = true;

    // check the neighbor of the position
    dfs(row+1, col, state_matrix, visited, current_language);
    dfs(row-1, col, state_matrix, visited, current_language);
    dfs(row, col+1, state_matrix, visited, current_language);
    dfs(row, col-1, state_matrix, visited, current_language);
}

int main() {
    int num_test_case;
    cin >> num_test_case;

    for (int i = 0; i < num_test_case; i++) {
        int row, col;
        cin >> row >> col;

        vector<vector<char>> state_matrix(row, vector<char>(col));
        for (int j = 0; j < row; j++) {
            for (int k = 0; k < col; k++) {
                cin >> state_matrix[j][k];
            }
        }

        vector<vector<bool>> visited(row, vector<bool>(col, false));
        map<char, int> language_state;
        for (int j = 0; j < row; j++) {
            for (int k = 0; k < col; k++) {
                if (!visited[j][k]) {

                    // find new state
                    char current_language = state_matrix[j][k];
                    language_state[current_language]++;
                    dfs(j, k, state_matrix, visited, current_language);
                }
            }
        }

        // change map to vector for sorting
        vector<pair<char, int>> sort_language_state;
        for (auto const& pair : language_state) {
            sort_language_state.push_back(pair);
        }

        // sort the languages by their state counts
        for (int j = 0; j < sort_language_state.size(); j++) {
            for (int k = j+1; k < sort_language_state.size(); k++) {
                if (sort_language_state[j].second < sort_language_state[k].second) {
                    swap(sort_language_state[j], sort_language_state[k]);
                } 
                if (sort_language_state[j].second == sort_language_state[k].second) {
                    if (sort_language_state[j].first > sort_language_state[k].first) {
                        swap(sort_language_state[j], sort_language_state[k]);
                    }
                }
            }
        }

        cout << "World #" << i+1 << endl;
        for (const auto& [language, count] : sort_language_state) {
            cout << language << ": " << count << endl;
        }

    }
    return 0;
}