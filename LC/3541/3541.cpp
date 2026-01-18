// link of question: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/
class Solution {
public:
    int maxFreqSum(string s) {
        vector<pair<char, int>> vowel;
        vector<pair<char, int>> consonant;
        bool is_find = false;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u') {
                for (int j = 0; j < vowel.size(); j++) {
                    if (s[i] == vowel[j].first) {
                        vowel[j].second++;
                        is_find = true;
                        break;
                    }
                }
                if (is_find) {
                    is_find = false;
                } else {
                    vowel.push_back({s[i], 1});
                }
            } else {
                for (int j = 0; j < consonant.size(); j++) {
                    if (s[i] == consonant[j].first) {
                        consonant[j].second++;
                        is_find = true;
                        break;
                    }
                }
                if (is_find) {
                    is_find = false;
                } else {
                    consonant.push_back({s[i], 1});
                }
            }
        }

        int max_vowel_value = 0;
        for (int i = 0; i < vowel.size(); i++) {
            if (max_vowel_value < vowel[i].second) {
                max_vowel_value = vowel[i].second;
            }
        }

        int max_consonant_value = 0;
        for (int i = 0; i < consonant.size(); i++) {
            if (max_consonant_value < consonant[i].second) {
                max_consonant_value = consonant[i].second;
            }
        }

        return max_vowel_value + max_consonant_value;
    }
};