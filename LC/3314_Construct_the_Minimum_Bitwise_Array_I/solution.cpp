class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        for (auto& num: nums) {
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                int diff = ((num+1) & -(num+1)) >> 1;
                ans.push_back(num - diff);
            }
        }

        return ans;
    }
};