class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int change = 0;
        int n = nums.size();

        if (n < 4 || nums[0] > nums[1]) {
            return false;
        }

        for (int i = 0; i < nums.size()-1; i++) {
            if (change % 2 == 0 && nums[i] > nums[i+1]) {
                change++;
            } else if (change % 2 == 1 && nums[i] < nums[i+1]) {
                change++;
            } else if (nums[i] == nums[i+1]) {
                return false;
            }
        }

        return change == 2;
    }
};