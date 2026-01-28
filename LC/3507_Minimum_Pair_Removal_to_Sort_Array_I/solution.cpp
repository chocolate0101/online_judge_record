class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int operations = 0;
        while (true) {
            bool is_sorted = true;
            for (int i = 0; i < nums.size()-1; i++) {
                if (nums[i] > nums[i+1]) {
                    is_sorted = false;
                    break;
                }
            }

            if (is_sorted) {
                return operations;
            }

            int min_pair_sum = INT_MAX;
            int min_pair_idx = 0;
            int tmp = 0;
            for (int i = 0; i < nums.size()-1; i++) {
                tmp = nums[i] + nums[i+1];
                if (tmp < min_pair_sum) {
                    min_pair_sum = tmp;
                    min_pair_idx = i;
                }
            }

            nums[min_pair_idx] = min_pair_sum;
            nums.erase(nums.begin() + min_pair_idx + 1);
            operations++;
        }
    }
}; 