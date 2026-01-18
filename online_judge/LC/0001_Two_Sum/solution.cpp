// link of the question：https://leetcode.com/problems/two-sum/

// solution 1
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};
    }
};

// solution 2
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            int to_find = target - nums[i];
            if (seen.count(to_find)) {
                return {i, seen[to_find]};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};

