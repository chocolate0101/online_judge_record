/*
Tight words

UVA 上有誤
UVA 10081：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1022
GPE 考古：10637
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int num_alphabet, len;
    while (cin >> num_alphabet >> len) {
        // initial
        vector<vector<long long int>> dp(len+1, vector<long long int>(num_alphabet+1, 0));
        for (int i = 0; i <= num_alphabet; i++) {
            dp[1][i] = 1;
        }

        for (int i = 2; i <= len; i++) {
            for (int j = 0; j < dp[i].size(); j++) {
                if (j == 0) {
                    dp[i][j] = dp[i-1][j] + dp[i-1][j+1];
                } else if (j == num_alphabet) {
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1];
                }
            }
        }

        long long int total_tight_word = 0;
        for (int i = 0; i <= num_alphabet; i++) {
            total_tight_word += dp[len][i];
        }

        long long int total_word = 1;
        for (int i = 0; i < len; i++) {
            total_word *= num_alphabet+1;
        }

        double percentage = (double)total_tight_word / total_word * 100;
        cout << fixed << setprecision(5) << percentage << endl;
    }
    return 0;
}