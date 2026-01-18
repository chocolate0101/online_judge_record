/*
Power Crisis

UVA 151：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=87
ZeroJudge q891：https://zerojudge.tw/ShowProblem?problemid=q891
GPE 考古：21944
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    while (cin >> n && n != 0) {
        for (int m = 1; ; m++) {
            // initialize the input
            vector<int> region(n);
            for (int i = 0; i < n; i++) {
                region[i] = i+1;
            }

            int shut_down_region = 0;
            region.erase(region.begin());

            while (region.size() > 1) {
                shut_down_region = (shut_down_region + m - 1) % region.size();
                if (region[shut_down_region] == 13) {
                    break;
                }

                region.erase(region.begin() + shut_down_region);
            }

            if (region.size() == 1) {
                cout << m << endl;
                break;
            }
        }
    }

    return 0;
}