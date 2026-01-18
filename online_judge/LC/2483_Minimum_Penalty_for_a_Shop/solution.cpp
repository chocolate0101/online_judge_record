// solution 1 (1D Dynamic Programming)
class Solution {
public:
    int bestClosingTime(string customers) {
        vector<int> best_score_dp;
        int index = 0, best_score = 0, best_hour = 0;
        best_score_dp.push_back(0);
        for (auto& customer: customers) {
            index++;
            if (customer == 'Y') {
                best_score_dp.push_back(best_score_dp[index-1] + 1);
            } else {
                best_score_dp.push_back(best_score_dp[index-1] - 1);
            }

            if (best_score_dp[index] > best_score) {
                best_score = best_score_dp[index];
                best_hour = index;
            }
        }

        return best_hour;
    }
};

// solution 2 (Prefix Sum)
class Solution {
public:
    int bestClosingTime(string customers) {
        int current_score = 0;
        int best_hour = 0, best_score = 0;
        int index = 0;
        for (auto &customer: customers) {
            index++;
            if (customer == 'Y') {
                current_score++;
            } else {
                current_score--;
            }

            if (current_score > best_score) {
                best_hour = index;
                best_score = current_score;
            }
        }

        return best_hour;
    }
};