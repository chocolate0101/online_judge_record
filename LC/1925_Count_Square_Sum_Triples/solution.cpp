// link of the problem: https://leetcode.com/problems/count-square-sum-triples/

// solution 1
class Solution {
public:
    int countTriples(int n) {
        set<int> square_sum;
        for (int i = 1; i <= n; i++) {
            square_sum.insert(i * i);
        }

        int count = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int tmp_square_sum = i * i + j * j;
                if (square_sum.count(tmp_square_sum)) {
                    if (i == j) {
                        count++;
                    } else {
                        count += 2;
                    }
                } else if (tmp_square_sum > n * n){
                    break;
                }
            }
        }

        return count;
    }
};

// solution 2
class Solution {
public:
    int countTriples(int n) {
        int squares[n+1];
        int count = 0;
        int left, right, sum;

        for (int i = 0; i < n+1; ++i) {
            squares[i] = i * i;
            left = 0;
            right = i - 1;
            while (left < right) {
                sum = squares[left] + squares[right];
                if (sum == squares[i]) {
                    count += 2;
                    left++;
                    continue;
                }

                if (sum < squares[i]) {
                    left++;
                    continue;
                }

                right--;
            }
        }

        return count;
    }
};