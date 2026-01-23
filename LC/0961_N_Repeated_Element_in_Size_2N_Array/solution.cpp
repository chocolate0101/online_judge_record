// solution 1
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        unordered_set<int> num_set = {};
        for (auto& num: nums) {
            if (num_set.count(num)) {
                return num;
            } else {
                num_set.insert(num);
            }
        }

        return nums[0];
    }
};

// solution 2 (best solution)
class Solution {
public:
    int repeatedNTimes(vector<int>& nums) {
        for (int i = 0; i < nums.size() - 2; i++) {
            if (nums[i] == nums[i+1] || nums[i] == nums[i+2]) {
                return nums[i];
            }
        }

        return nums[nums.size()-1];
    }
};