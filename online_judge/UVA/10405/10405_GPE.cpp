/*
Longest Common Subsequence

UVA 上有誤
UVA 10405：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1346
ZeroJudge c001：https://zerojudge.tw/ShowProblem?problemid=c001
GPE 考古：11017

思考邏輯：列出 str1 所有 substring 的可能，將其與 str2 一一比對並找出最長的
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int max_len = 0;
    string str1;
    while (cin >> str1) {
        string str2, sub_sequence;
        cin >> str2;
        for (int mask = 0; mask < (1 << str1.length()); mask++) {
            sub_sequence = "";
            for (int i = 0 ; i < str1.length(); i++) {
                if (mask & (1 << i)) {
                    sub_sequence += str1[i];
                }
            }
            int k = 0; int j = 0;
            while (k < sub_sequence.length() && j < str2.length()) {
                if (sub_sequence[k] == str2[j]) {
                    k++;
                }
                j++;
            }
            if (k == sub_sequence.length()) {
                max_len = max(max_len, (int)sub_sequence.length());
            }
        }
        cout << max_len << "\n";
    }

    return 0;
}