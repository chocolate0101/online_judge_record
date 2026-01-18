// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_set<int> unique_num;
        vector<int> duplicate_num;
        for (int i = 0; i < nums.size(); i++) {
            if (unique_num.find(nums[i]) == unique_num.end()) {
                unique_num.insert(nums[i]);
            } else {
                duplicate_num.push_back(nums[i]);
            }
        }

        return  duplicate_num;
    }
};