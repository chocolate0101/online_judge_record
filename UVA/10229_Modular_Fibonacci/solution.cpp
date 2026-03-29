#include <bits/stdc++.h>
using namespace std;

int main() {
    long long n, m;
    while (cin >> n >> m) {
        if (m == 0 || n == 0) {
            cout << 0 << endl;
        } else {
            long long period = 3 * (1 << (m-1));
            n %= period;
            long long module = 1 << m;

            long long prev = 0;
            long long prev_prev = 1;
            long long cur = 0;

            for (int i = 0; i < n; i++) {
                cur = (prev + prev_prev) % module;
                prev_prev = prev;
                prev = cur;
            }

            cout << cur << endl;
        }
    }

    return 0;
}