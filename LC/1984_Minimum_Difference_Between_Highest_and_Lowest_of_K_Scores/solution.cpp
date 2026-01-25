class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        int min_diff = INT_MAX;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size()-k+1; i++) {
            int tmp = nums[i+k-1] - nums[i];
            if (tmp < min_diff) {
                min_diff = tmp;
            }
        }

        return min_diff;
    }
};