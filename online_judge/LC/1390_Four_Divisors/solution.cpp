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
                        for (int j = 2; j < sqrt(div2)+1; j++) {
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