// link of the question: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/

class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int have_one = 0, prev_idx = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 1) {
                prev_idx = i;
                have_one = 1;
                break;
            }
        }

        if (!have_one) {
            return true;
        }
        
        for (int i = prev_idx+1; i < nums.size(); i++) {
            if (nums[i] == 1) {
                if (i - prev_idx - 1 < k) {
                    return false;
                }
                prev_idx = i;
            }
        }

        return true;
    }
};