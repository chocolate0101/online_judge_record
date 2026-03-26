#include <bits/stdc++.h>
using namespace std;

int main() {
    long long cases;
    cin >> cases;

    for (long long i = 1; i < cases + 1; i++) {
        long long num;
        cin >> num;

        long long tmp = num;

        unordered_set<int> record;
        record.insert(tmp);

        while (1) {
            long long square_sum = 0;
            while (tmp > 0) {
                square_sum += pow(tmp % 10, 2);
                tmp /= 10;
            }

            if (square_sum == 1) {
                cout << "Case #" << i << ": " << num << " is a Happy number.\n";
                break;
            } else if (record.count(square_sum) == 1) {
                cout << "Case #" << i << ": " << num << " is an Unhappy number.\n";
                break;
            } else {
                record.insert(square_sum);
            }
        
            tmp = square_sum;
        }
    }

    return 0;
}