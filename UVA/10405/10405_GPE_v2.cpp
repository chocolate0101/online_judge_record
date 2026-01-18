/*
Longest Common Subsequence

UVA 上有誤
UVA 10405：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1346
ZeroJudge c001：https://zerojudge.tw/ShowProblem?problemid=c001
GPE 考古：11017

令 str1 = sub1 + e1, str2 = sub2 + e2
其中 e1 和 e2 分別為 str1 和 str2 的最後一個字元
則會有以下四種狀況：

cond.1 (e1 和 e2 都不是 LCS 的一部份)
LCS(str1, str2) = LCS(sub1, sub2)

cond.2 (e1 是 LCS 的一部份但 e2 不是)
LCS(str1, str2) = LCS(str1, sub2)

cond.3 (e1 不是 LCS 的一部份但 e2 是)
LCS(str1, str2) = LCS(sub1, str2)

cond.4 (e1 和 e2 都是 LCS 的一部份)
LCS(str1, str2) = LCS(sub1, sub2) + e1

可將四種情況整合成
LCS(str1 ,str2) = max(LCS(sub1, sub2), LCS(str1, sub2), LCS(sub1, str2))    if e1 != e2
LCS(str1, str2) = LCS(sub1, sub2) + e1                                      if e1 == e2
*/


#include <bits/stdc++.h>
using namespace std;

int main() {
    int max_len = 0;
    string str1;
    while (cin >> str1) {
        string str2;
        cin >> str2;

        vector<vector<int>> dp_matrix(str1.length()+1, vector<int> (str2.length() + 1, 0));
        for(int i = 0; i < str1.length(); i++) {
            dp_matrix[i][0] = 0;
        }
        for(int i = 0; i < str2.length(); i++) {
            dp_matrix[0][i] = 0;
        }

        for (int i = 1; i < str1.length()+1; i++) {
            for (int j = 1; j < str2.length()+1; j++) {
                if (str1[i-1] == str2[j-1]) {
                    dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1;
                } else {
                    dp_matrix[i][j] = max(dp_matrix[i-1][j], dp_matrix[i][j-1]);
                }
            }
        }
        cout << dp_matrix[str1.length()][str2.length()] << "\n";
    }

    return 0;
}