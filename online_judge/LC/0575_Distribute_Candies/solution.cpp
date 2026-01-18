// link of the question: https://leetcode.com/problems/distribute-candies/

class Solution {
public:
    int distributeCandies(vector<int>& candyType) {
        unordered_set<int> unique_candy_type(candyType.begin(), candyType.end());

        if (unique_candy_type.size() <= candyType.size() / 2) {
            return unique_candy_type.size();
        } else {
            return candyType.size() / 2;
        }
    }
};