/* 
B-2 Sequence

UVA 11063：https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2004
ZeroJudge d123：https://zerojudge.tw/ShowProblem?problemid=d123
*/

#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, case_num = 0, is_B2_sequence = 1;
	
	while(cin >> n) {
		case_num++;
        vector<int> num(n);

        // input the number and check whether input is bigger than 1
		for (int i = 0; i < n; i++) {
			cin >> num[i];
            if (num[i] < 1) {
                is_B2_sequence = 0;
            }
		}

        // check whether the number's sequence is increasing
        if (is_B2_sequence) {
            for (int i = 0; i < n-1; i++) {
                if ( !(num[i] < num[i+1]) ) {
                    is_B2_sequence = 0;
                    break;
                }
            }
        }
		
        // check whether all numbers' two sum is different
		if (is_B2_sequence) {
            unordered_set<int> two_sum;
            for (int i = 0; i < n; i++) {
                for (int j = i; j < n; j++) {
                    int sum = num[i] + num[j];
                    if (two_sum.count(sum) == 0) {
                        two_sum.insert(sum);
                    } else {
                        is_B2_sequence = 0;
                        break;
                    }
                }
                if (!is_B2_sequence) {
                    break;
                }
            }
        }
        
        // print the answer
		if (is_B2_sequence) {
			cout << "Case " << "#" << case_num <<": It is a B2-Sequence.\n\n";
		} else {
			cout << "Case " << "#" << case_num <<": It is not a B2-Sequence.\n\n";
		}
		is_B2_sequence = 1;
	}
	
	return 0;
}