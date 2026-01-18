// link of the question: https://leetcode.com/problems/number-of-substrings-with-only-1s/description/

class Solution {
public:
    int numSub(string s) {
        long long ans = 0, count_one = 0;
        for (char ch: s) {
            if (ch == '1') {
                count_one++;
            } else {
                ans += (count_one + 1) * count_one / 2;
                count_one = 0;
            }
        }
        
        ans += (count_one + 1) * count_one / 2;
        ans %= 1000000007;
        return ans;
    }
};