/*
Digits Primes

UVA 10533：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1474
ZeroJudge d438：https://zerojudge.tw/ShowProblem?problemid=d438
GPE 考古：11028


sieve of eratosthenes 高效找質數的演算法
思考邏輯：
step1. 先用一個陣列將全部數字預設成質數
step2. 從 2 開始，將其平方後的所有倍數都當成合數，將其對應的位置設成非質數
step3. 計算每個 prime 是否為 digit prime
step4. 再開一個陣列計算每一個數前共有幾個 digit prime
step4. 根據起始和結束位置相減求得 digit prime 數量
*/


#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, start, end;
    cin >> n;
    bool is_prime[1000001];
    int count_prime[1000001] = {0};

    for (int i = 2; i < 1000001; i++) {
        is_prime[i] = 1;
    }
    is_prime[0] = 0;
    is_prime[1] = 0;

    for (int i = 2; i <= sqrt(1000000); i++) {
        if (is_prime[i]) {
            int k = i * i;
            while(k <= 1000000) {
                is_prime[k] = 0;
                k += i;
            }
        }
    }

    for (int i = 1; i <= 1000000; i++) {
        if (is_prime[i]) {
            int k = i, sum = 0;
            while(k) {
                sum += k % 10;
                k /= 10;
            }
            if (is_prime[sum]) {
                count_prime[i] = count_prime[i-1] + 1;
            } else {
                count_prime[i] = count_prime[i-1];
            }
        } else {
            count_prime[i] = count_prime[i-1];
        }
    }

    for (int i = 0; i < n; i++) {
        cin >> start >> end;
        cout << count_prime[end] - count_prime[start-1] << "\n";
    }
    
    return 0;
}