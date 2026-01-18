// link of the question: https://leetcode.com/problems/jewels-and-stones/description/

class Solution {
public:
    int numJewelsInStones(string Jewels, string stones) {
        unordered_set<char> jewels_set(jewels.begin(), jewels.end());
        int total_jewel = 0;

        for (char stone: stones) {
            if (jewels_set.find(stone) != jewels_set.end()) {
                total_jewel++;
            }
        }

        return total_jewel;
    }
}