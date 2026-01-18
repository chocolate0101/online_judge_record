/*
Quirksome Squares

UVA 00256：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=192
ZeroJudge d182：https://zerojudge.tw/ShowProblem?problemid=d182
GPE 考古：22351
*/


/*
思考邏輯：
符合結果的數一定是平方數 (因為 N = (a+b)^2 所以 N 本身是平方數)
因此不需要跑完整個數列，僅需要檢查是否平方數是否符合條件
而 N 位數的平方數只需要測試 N/2 位數數字所組成的平方數即可
證明請看附檔
*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, left, right, sum;
    long long int ans;
    while(cin >> n) {
        if (n == 2) {
            for (int i = 0; i <= 9; i++) {
                ans = i * i;
                left = ans % 10;
                right = ans / 10;
                sum = left + right;
                if (sum * sum == ans) {
                    cout << setfill('0') << setw(2) << ans << "\n";
                }
            }
        } else if (n == 4) {
            for (int i = 0; i <= 99; i++) {
                ans = i * i;
                left = ans % 100;
                right = ans / 100;
                sum = left + right;
                if (sum * sum == ans) {
                    cout << setfill('0') << setw(4) << ans << "\n";
                } 
            }
        } else if (n == 6) {
            for (int i = 0; i <= 999; i++) {
                ans = i * i;
                left = ans % 1000;
                right = ans / 1000;
                sum = left + right;
                if (sum * sum == ans) {
                    cout << setfill('0') << setw(6) << ans << "\n";
                } 
            }
        } else {
            for (int i = 0; i <= 9999; i++) {
                ans = i * i;
                left = ans % 10000;
                right = ans / 10000;
                sum = left + right;
                if (sum * sum == ans) {
                    cout << setfill('0') << setw(8) << ans << "\n";
                } 
            }
        }
    }

    return 0;
}