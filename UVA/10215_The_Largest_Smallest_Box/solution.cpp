#include <bits/stdc++.h>
using namespace std;

int main() {
    double l, w;
    while (cin >> l >> w) {
        double tmp = pow(l, 2) + pow(w, 2) - l * w;
        double x = ((l + w) - sqrt(tmp)) / 6;
        double min_1 = min(l, w) / 2;

        cout << fixed << setprecision(3);
        cout << x << " 0.000 " << min_1 << endl;
    }

    return 0;
}