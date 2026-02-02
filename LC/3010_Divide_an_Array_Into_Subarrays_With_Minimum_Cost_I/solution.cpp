class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int min_1 = INT_MAX, min_2 = INT_MAX;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < min_1) {
                min_2 = min_1;
                min_1 = nums[i];
            } else if (nums[i] < min_2) {
                min_2 = nums[i];
            }
        }

        return nums[0] + min_1 + min_2;
    }
};