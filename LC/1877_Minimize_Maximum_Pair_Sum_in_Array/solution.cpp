// solution 1 (can't not pass)
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int n = nums.size();
        int max_sum_pair = INT_MAX;
        sort(nums.begin(), nums.end());
        
        do {
            int curr_pair_sum = 0;

            for (int i = 0; i < n; i+=2) {
                int tmp = nums[i] + nums[i+1];
                curr_pair_sum = max(curr_pair_sum, tmp);
            }

            max_sum_pair = min(max_sum_pair, curr_pair_sum);
        } while (next_permutation(nums.begin(), nums.end()));

        return max_sum_pair;
    }
};

// solution 2
class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int max_sum_pair = INT_MIN;
        int n = nums.size();
        for (int i = 0; i < n / 2; i++) {
            int tmp = nums[i] + nums[n-i-1];
            max_sum_pair = max(tmp, max_sum_pair);
        }

        return max_sum_pair;
    }
};