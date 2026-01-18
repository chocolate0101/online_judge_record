/*
Count the Trees

請先安裝 boost multiprecision
sudo apt update
sudo apt install libboost-all-dev
*/

// 使用 C++ 之大數字套件
#include <bits/stdc++.h>
#include <boost/multiprecision/cpp_int.hpp>
using namespace std;
using namespace boost::multiprecision;

int main() {
    int n;
    while (cin >> n) {
        //terminal condition
        if (n == 0) {
            break;
        }

        cpp_int ans = 1;
        for (int i = n+2; i <= 2*n; i++) {
            ans *= i;
        }

        cout << ans << endl;
    }
    return 0;
}

// 不使用 C++ 內建式大數字
#include <bits/stdc++.h>
using namespace std;

class BinInt {
public:
    string value;

    BinInt(long long val = 0) {
        if (val == 0) {
            value = "0";
        } else {
            value = to_string(val);
        }
    }

    BinInt(string s) {
        value = s;
    }

    BinInt operator*(const BinInt& other) const {
        string num1 = this->value;
        string num2 = other.value;
        int n1 = num1.size();
        int n2 = num2.size();
        if (num1 == "0" || num2 == "0") {
            return BinInt("0");
        } 
        
        vector<int> result(n1+n2, 0);
        
        for (int i = n1-1; i >= 0; i--) {
            for (int j = n2 -1; j >=0; j--) {
                int mul = (num1[i] - '0') * (num2[j] - '0');
                int sum = mul + result[i + j + 1];
                result[i + j + 1] = sum % 10;
                result[i + j] += sum / 10;
            }
        }

        string s = "";
        int i = 0;
        while (i < result.size() && result[i] == 0) {
            i++;
        }
        while (i < result.size()) {
            s += to_string(result[i]);
            i++;
        }
        return BinInt(s);
    }

    friend ostream& operator<<(ostream& os, const BinInt& bi) {
        os << bi.value;
        return os;
    }
};

int main() {
    int n;
    while (cin >> n) {
        //terminal condition
        if (n == 0) {
            break;
        }

        BinInt ans = 1;
        for (int i = n+2; i <= 2*n; i++) {
            ans = ans * i;
        }

        cout << ans << endl;
    }
    return 0;
}