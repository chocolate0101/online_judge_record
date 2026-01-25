// solution 1
class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int sum_divisor = 0;
        for (auto& num: nums) {
            int num_divisor = 0;
            int current_sum_divisor = 0;
            int limit_num = sqrt(num) + 1;
            for (int i = 1; i < limit_num; i++) {
                if (num == i * i) {
                    current_sum_divisor += i;
                    num_divisor++;
                } else if (num % i == 0) {
                    current_sum_divisor += i;
                    current_sum_divisor += num / i;
                    num_divisor += 2;
                }

                if (num_divisor > 4) {
                    break;
                }
            }

            if (num_divisor == 4) {
                sum_divisor += current_sum_divisor;
            }
        }

        return sum_divisor;
    }
};

// solution 2
class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int large_num = *max_element(nums.begin(), nums.end());
        int ans = 0;
        vector<pair<int, int>> divisor_list(large_num+1, {0, 0}); // {count_divisor, sum_divisor}

        for (int i = 1; i < large_num+1; i++) {
            for (int j = i; j < large_num+1; j += i) {
                divisor_list[j].first += 1;
                divisor_list[j].second += i;
            }
        }

        for (auto& num: nums) {
            if (divisor_list[num].first == 4) {
                ans += divisor_list[num].second;
            }
        }

        return ans;
    }
};

// solution 3 (best solution)
class Solution {
public:
    int sumFourDivisors(vector<int>& nums) {
        int ans = 0;
        for (auto& num: nums) {
            if (num < 6) {
                continue;
            }

            int limit = int(sqrt(num));
            for (int i = 2; i < limit+1; i++) {
                if (num % i == 0) {
                    int div1 = i;
                    int div2 = num / i;

                    if (div1 == div2) {
                        break;
                    }

                    bool div2_is_prime = true;
                    if (div1 * div1 == div2) {
                        ans += 1 + num + div1 + div2;
                    } else {
                        int limit_div2 = sqrt(div2) + 1;
                        for (int j = 2; j < limit_div2; j++) {
                            if (div2 % j == 0) {
                                div2_is_prime = false;
                                break;
                            }
                        }

                        if (div2_is_prime) {
                            ans += 1 + num + div1 + div2;
                        }
                    }

                    break;
                }
            }
        }

        return ans;
    }
};