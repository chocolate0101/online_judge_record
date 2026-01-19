// solution 1 (1D Dynamic Programming)
class Solution {
public:
    int bestClosingTime(string customers) {
        vector<int> best_score = {0};
        for (auto& customer: customers) {
            if (customer == 'Y') {
                best_score.push_back(best_score.back() + 1);
            } else {
                best_score.push_back(best_score.back() - 1);
            }
        }

        int max_score = INT_MIN;
        int best_hour = 0;
        for (int i = 0; i < best_score.size(); i++) {
            if (best_score[i] > max_score) {
                max_score = best_score[i];
                best_hour = i;
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