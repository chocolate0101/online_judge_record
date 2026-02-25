class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        vector<pair<int, int>> ans_pair;
        for (auto& num: arr) {
            int count_one = __builtin_popcount(num);
            ans_pair.push_back({count_one, num});
        }

        sort(ans_pair.begin(), ans_pair.end());
        
        vector<int> ans;
        for (auto& pair: ans_pair) {
            ans.push_back(pair.second);
        }
        return ans;
    }
};