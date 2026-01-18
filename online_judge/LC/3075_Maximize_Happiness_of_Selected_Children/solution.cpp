// solution 1: (Greedy)
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end(), greater<int>());
        long long total_value = 0;

        for (int i = 0; i < k; i++) {
            long long tmp = happiness[i] - i;
            if (tmp <= 0) {
                break;
            }
            total_value += tmp;
        }

        return total_value;
    }
};

// solution 2: (min-heap)
class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        // <data type, container, comparison method>
        // vector<int>：底層實作方式是用 vector 實作
        // greater<int>：讓小的值在上方
        // 因為 priority_queue 的第三個 parameter 預設是 less<int>
        // 因此需要修改成 min-heap
        priority_queue<int, vector<int>, greater<int>> pq;

        for (int h: happiness) {
            if (pq.size() < k) {
                pq.push(h);
            } else if (h > pq.top()) {
                pq.pop();
                pq.push(h);
            }
        }

        long long total_value = 0;
        for (int i = k - 1; i >= 0; i--) {
            int tmp = pq.top();
            pq.pop();

            if (tmp - i > 0) {
                total_value += tmp - i;
            }
        }

        return total_value;
    }
};