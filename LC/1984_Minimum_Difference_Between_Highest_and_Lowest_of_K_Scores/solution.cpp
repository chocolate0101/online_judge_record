// solution 1
class Solution {
public:
    void backtrack(vector<int>& nums, int start_index, vector<int>& curr_comb, int& min_diff, int k, int n) {
        if (curr_comb.size() == k) {
            int curr_diff = *max_element(curr_comb.begin(), curr_comb.end()) - *min_element(curr_comb.begin(), curr_comb.end());
            min_diff = min(min_diff, curr_diff);
            return;
        }

        for (size_t i = start_index; i < n; i++) {
            curr_comb.push_back(nums[i]);
            backtrack(nums, i+1, curr_comb, min_diff, k, n);
            curr_comb.pop_back();
        }
    }

    int minimumDifference(vector<int>& nums, int k) {
        int min_diff = INT_MAX;
        int n = nums.size();
        vector<int> curr_comb;
        backtrack(nums, 0, curr_comb, min_diff, k, n);

        return min_diff;
    }
};

// solution 2
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