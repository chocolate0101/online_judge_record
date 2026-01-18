// link of the question: https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/

class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        int total_beam = 0;
        int previous_security_device = 0;

        for (int i = 0; i < bank.size(); i++) {
            int current_security_device = 0;
            for (char chr: bank[i]) {
                if (chr == '1') {
                    current_security_device += 1;
                }
            }
            if (current_security_device != 0) {
                total_beam += current_security_device * previous_security_device;
                previous_security_device = current_security_device;
            }

        }
        return total_beam;
    }
};