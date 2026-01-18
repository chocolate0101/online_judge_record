// link of the question: https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/

class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        unordered_set<char> jewel_set(jewels.begin(), jewels.end());
        int total_jewel = 0;

        for (char stone: stones) {
            if (jewel_set.find(stone) != jewel_set.end()) {
                total_jewel++;
            }
        }

        return total_jewel;
    }
};