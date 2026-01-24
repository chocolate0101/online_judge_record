class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        unordered_set<int> max_sum_pair;
        int n = nums.size();
        for (int i = 0; i < n / 2; i++) {
            int tmp = nums[i] + nums[n-i-1];
            max_sum_pair.insert(tmp);
        }

        return *max_element(max_sum_pair.begin(), max_sum_pair.end());
    }
};