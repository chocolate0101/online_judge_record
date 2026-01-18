/*
Lotto

UVA 441：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=382
ZeroJudge c074：https://zerojudge.tw/ShowProblem?problemid=c074 
*/ 

#include <bits/stdc++.h>
using namespace std;

void find_set(const vector<int>& subset, int k, int start, vector<int>& current_set) {
    if (current_set.size() == k) {
        for (int i = 0; i < k-1; i++) {
            cout << current_set[i] << " ";
        }
        cout << current_set[k-1] <<endl;
    }

    for (int i = start; i < subset.size(); i++) {
        current_set.push_back(subset[i]);
        find_set(subset, k, i+1, current_set);
        current_set.pop_back();
    }
}

int main() {
    int n, k = 6, first = 1;
    while (cin >> n) {
        if (n == 0) break;
        else if (first) {
            first = 0;
        } else {
            cout << endl;
        }

        // input the subset
        vector<int> subset(n);
        for(int i = 0; i < n; i++) {
            cin >> subset[i];
        }

        // recursive the function
        vector<int> current_set;
        find_set(subset, k, 0, current_set);

    }

    return 0;
}