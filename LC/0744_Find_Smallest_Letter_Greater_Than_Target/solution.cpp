// solution 1
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        for (auto& letter: letters) {
            if (letter > target) {
                return letter;
            }
        }

        return letters[0];
    }
};
// solution 2
class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        int i = 0, j = letters.size()-1, mid = 0;

        if (target >= letters[j] || target < letters[0]) {
            return letters[0];
        }

        while (i <= j) {
            mid = (i + j) / 2;
            if (letters[mid] <= target) {
                i = mid + 1;
            } else {
                j = mid - 1;
            }
        }

        return letters[i];
    }
};