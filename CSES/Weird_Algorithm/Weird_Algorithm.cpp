/*
Weird Algorithm (Collatz Conjecture)

CSES Weird Algorithm：https://cses.fi/alon/task/1068/
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
    long long int n;
    cin >> n;
    while (1) {
        cout << n << " ";
        if (n == 1) {
            break;
        } else if (n % 2 == 0) {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
    }
}