// solution 1
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int min_abs_diff = INT_MAX;
        vector<vector<int>> min_abs_diff_list;

        for (int i = 0; i < arr.size(); i++) {
            for (int j = i+1; j < arr.size(); j++) {
                int tmp = abs(arr[i] - arr[j]);
                if (tmp < min_abs_diff) {
                    min_abs_diff = tmp;
                    min_abs_diff_list.clear();
                    if (arr[i] < arr[j]) {
                        min_abs_diff_list.push_back({arr[i], arr[j]});
                    } else {
                        min_abs_diff_list.push_back({arr[j], arr[i]});
                    }
                } else if (tmp == min_abs_diff) {
                    if (arr[i] < arr[j]) {
                        min_abs_diff_list.push_back({arr[i], arr[j]});
                    } else {
                        min_abs_diff_list.push_back({arr[j], arr[i]});
                    }
                }
            }
        }

        sort(min_abs_diff_list.begin(), min_abs_diff_list.end());
        return min_abs_diff_list;
    }
};

// solution 2
class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        int min_abs_diff = INT_MAX;
        vector<vector<int>> min_abs_diff_list;
        sort(arr.begin(), arr.end());

        for (int i = 0; i < arr.size()-1; i++) {
            int tmp = arr[i+1] - arr[i];
            if (tmp < min_abs_diff) {
                min_abs_diff = tmp;
                min_abs_diff_list.clear();
                min_abs_diff_list.push_back({arr[i], arr[i+1]});
            } else if (tmp == min_abs_diff) {
                min_abs_diff_list.push_back({arr[i], arr[i+1]});
            }
        }

        return min_abs_diff_list;
    }
};