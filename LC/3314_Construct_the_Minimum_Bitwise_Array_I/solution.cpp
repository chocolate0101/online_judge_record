// solution 1
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        bool is_find = 0;
        for (auto& num: nums) {
            is_find = 0;
            for (int i = 0; i < num; i++) {
                if ((i | (i+1)) == num) {
                    ans.push_back(i);
                    is_find = 1;
                    break;
                }
            }

            if (!is_find) {
                ans.push_back(-1);
            }
        }

        return ans;
    }
};

// solution 2 (best solution)
class Solution {
public:
    vector<int> minBitwiseArray(vector<int>& nums) {
        vector<int> ans;
        for (auto& num: nums) {
            if (num % 2 == 0) {
                ans.push_back(-1);
            } else {
                int diff = ((num+1) & -(num+1)) >> 1;
                ans.push_back(num - diff);
            }
        }

        return ans;
    }
};