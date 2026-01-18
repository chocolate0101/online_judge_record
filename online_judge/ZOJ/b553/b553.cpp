/*
Collatz Problem

ZeroJudge b553：https://zerojudge.tw/ShowProblem?problemid=b553
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int n;

    while(cin >> n) {
        int count = 0;
        while (1) {
            if (n == 1) {
                cout << count << endl;
                break;
            } else if (n % 2 == 0) {
                n /= 2;
                count++;
            } else {
                n = 3 * n + 1;
                count++;
            }
        }
    }
}