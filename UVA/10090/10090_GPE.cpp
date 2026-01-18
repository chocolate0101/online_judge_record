/*
Marbles

UVA 上有誤
UVA 10090：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=35&page=show_problem&problem=1031
ZeroJudge e594：https://zerojudge.tw/ShowProblem?problemid=e594
GPE 考古：10642

c1 * n1 + c2 * n2 = n
設 gcd(c1, c2) = g
則 c1  = g * m1, c2 = g * m2
原式 => g * m1 * n1 + g * m2 * n2 = n
    => g * (m1 * n1 + m2 * n2) = n
因此 n 一定是 g 的倍數

m1 * n1 + m2 * n2 = n / g
此為經典擴展歐幾里得演算法
*/

#include <bits/stdc++.h>
using namespace std;

long long int gcd_func(long long int a, long long int b, long long int& x, long long int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }

    long long int x1, y1;
    long long int d = gcd_func(b, a % b, x1, y1);
    x = y1;
    y = x1 - (a / b) * y1;
    return d;
}

int main() {
    long long int n, c1, n1, c2, n2;
    while(cin >> n && n != 0) {
        cin >> c1 >> n1;
        cin >> c2 >> n2;

        long long int m1, m2;
        long long int gcd = gcd_func(n1, n2, m1, m2);

        if (n % gcd != 0) {
            cout << "failded\n";
            continue;
        }

        // get particular solution
        long long int m1_particular = m1 * (n / gcd);
        long long int m2_particular = m2 * (n / gcd);

        // change particular solution to general solution
        long long int delta_m1 = n2 / gcd;
        long long int delta_m2 = n1 / gcd;

        long long int k_min, k_max;
        // k_min 必須大於等於 -m1_particular / delta_m1 
        // 因此直接將其取整，但因為 C++ 會自動刪除小數
        // 所以當 m1_particular 是正數時，表 k_min 現在要大於一個負數，但因為 C++ 會自動刪掉小數要額外處理 (a/b 的上界 = (a+b-1)/b 的下界)
        // 當 m1_particular 是負數時，表 k_min 現在要大於一個正數，剛好 C++ 有自動刪掉小數的功能，可直接帶入
        k_min = (m1_particular >= 0) ? (-m1_particular + delta_m1 - 1) / delta_m1 : -m1_particular / delta_m1;
        k_max = m2_particular / delta_m2;

        if (k_min > k_max) {
            cout << "failed\n";
            continue;
        }

        // 原式 => cost = m1 * c1 + m2 * c2
        // 又因為 m1 = m1_particular + k * delta_m1
        // m2 = m2_particular - k * delta_m2
        // 所以原式 => cost = (m1_particular + k * delta_m1) * c1 + (m2_particular - k * delta_m2) * c2
        //                 = (m1_particular * c1 + m2_particular * c2) + k * (delta_m1 * c1 - delta_m2 * c2)
        //                 = constant + k * slope
        // 因此當 slope > 0，則 k 越小 cost 越小，k 取 k_min，反之取 k_max
        long long int best_m1, best_m2;
        long long int slope = c1 * delta_m1 - c2 * delta_m2;

        if (slope >= 0) {
            long long int k = k_min;
            best_m1 = m1_particular + k * delta_m1;
            best_m2 = m2_particular - k * delta_m2;
        } else {
            long long int k = k_max;
            best_m1 = m1_particular + k * delta_m1;
            best_m2 = m2_particular - k * delta_m2;
        }

        cout << best_m1 << " " << best_m2 << endl;
    }

    return 0;
}