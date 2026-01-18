// link of the problem: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution {
public:
    int countOdds(int low, int high) {
        int low_odd = (low + 1) / 2;
        int high_odd = (high + 1) / 2;
        int count = high_odd - low_odd;
        if (low % 2 != 0) {
            count += 1;
        }
        return count;
    }
};