/*
Longest Increasing Subsequence

LC300：https://leetcode.com/problems/longest-increasing-subsequence/description/
GPE 考古：2015_09

思考邏輯：
從頭開始當成最長 LIS 的最後一個
若下一個比這個還大，則表示最長 LIS 可以再變長一個
若下個沒有比這個還大，則表示最長 LIS 維持在前面對大的 LIS 大小
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    while(cin >> n) {
        vector<int> int_seq;
        int tmp;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            int_seq.push_back(tmp);
        }
        
        vector<int> LIS(n, 1);
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (int_seq[i] > int_seq[j]) {
                    LIS[i] = max(LIS[i], LIS[j] + 1);
                }
            }
        }
        cout << *max_element(LIS.begin(), LIS.end()) << "\n";
    }

    return 0;
}