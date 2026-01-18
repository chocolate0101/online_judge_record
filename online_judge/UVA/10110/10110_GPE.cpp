/*
Light, more light

UVA 上有誤
UVA 10110：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=35&page=show_problem&problem=1051
ZeroJudge d111：https://zerojudge.tw/ShowProblem?problemid=d111
GPE 考古：10528
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    bool is_square_num = false;
    while (cin >> n && n != 0) {
        for (int i = 1; i < int(sqrt(n)+1); i++) {
            if (i * i == n) {
                is_square_num = true;
                cout << "yes\n";
                break;
            }
        }

        if (!is_square_num) {
            cout << "no\n";
        } else {
            is_square_num = false;
        }
    }
    return 0;
}