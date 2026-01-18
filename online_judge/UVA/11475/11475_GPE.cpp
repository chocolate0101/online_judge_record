/*
Extend to Palindromes

UVA 11475：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2470
ZeroJudge e595：https://zerojudge.tw/ShowProblem?problemid=e595
GPE 考古：24931
*/

#include <bits/stdc++.h>
using namespace std;

vector<int> compute_lps(const string& pattern) {
    int m = pattern.length();
    vector<int> lps(m, 0);
    int length = 0;
    int i = 1;

    while (i < m) {
        if (pattern[i] == pattern[length]) {
            length++;
            lps[i] = length;
            i++;
        } else {
            if (length != 0) {
                length = lps[length - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }
    return lps;
}

int main() {
    string words;
    while (cin >> words) {
        string words_reverse = words;
        reverse(words_reverse.begin(), words_reverse.end());
        
        // is palindrome itself
        if (words_reverse == words) {
            cout << words << endl;
            continue;
        }

        string combined = words_reverse + "#" + words;

        vector<int> lps = compute_lps(combined);
        int longest_palindrome_prefix_len = lps.back();

        cout << words << words_reverse.substr(longest_palindrome_prefix_len) << endl;
    }

    return 0;
}