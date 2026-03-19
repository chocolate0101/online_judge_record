#include <bits/stdc++.h>
using namespace std;

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; i++) {
        int start, end;
        long long total = 0;
        cin >> start;
        cin >> end;

        for (int j = start; j <= end; j++) {
            if (j % 2 == 0) { // even
                continue;
            } else { // odd
                total += j;
            }
        }

        cout << "Case " << i+1 << ": " << total << endl;
    }

    return 0;
}