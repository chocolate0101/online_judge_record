/*
Sumsets

UVA 10125：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1066
GPE 考古：10655

思考邏輯：如果單純用四個 loop 去找複雜度會過高。因此改成從最大可能的 d 開始看是否能組成，依序遞減直到找到為止。
*/


#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, is_find = 0;
    while(cin >> n) {
        if (n != 0) {
            vector<long long int> element(n);
            for (long long int i = 0; i < n; i++) {
                cin >> element[i];
            }
            sort(element.begin(), element.end());
            for (int l = element.size()-1; l >= 0 && !is_find; l--) {
                for (int i = 0; i < element.size() && !is_find; i++) {
                    if (i == l) continue;
                    for (int j = i+1; j < element.size() && !is_find; j++) {
                        if (j == l) continue;
                        for (int k = j+1; k < element.size() && !is_find; k++) {
                            if (k == l) continue;
                            if (element[i] + element[j] + element[k] == element[l]) {
                                cout << element[l] << "\n";
                                is_find = 1;
                                break;
                            }
                        }
                    }
                }
            }
            if (is_find) {
                is_find = 0;
            } else {
                cout << "no solution\n";
            }
        } else {
            break;
        }
        
    }
    
    return 0;
}