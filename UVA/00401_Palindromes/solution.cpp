#include <bits/stdc++.h>
using namespace std;

int main() {
    string str;
    while(cin >> str) {
        bool is_palindromes = true;
        bool is_mirror = true;
        int length = str.length();

        unordered_map<char, char> reversed_table = 
            {{'A', 'A'}, {'E', '3'}, {'H', 'H'}, {'I', 'I'}, {'J', 'L'}, {'L', 'J'},
            {'M', 'M'}, {'O', 'O'}, {'S', '2'}, {'T', 'T'}, {'U', 'U'}, {'V', 'V'},
            {'W', 'W'}, {'X', 'X'}, {'Y', 'Y'}, {'Z', '5'}, {'1', '1'}, {'2', 'S'},
            {'3', 'E'}, {'5', 'Z'}, {'8', '8'}};

        for (int i = 0; i < length; i++) {
            if (is_palindromes && str[i] != str[length - i -1]) {
                is_palindromes = false;
            }

            if (is_mirror) {
                if (reversed_table.find(str[i]) != reversed_table.end()) {
                    if (str[length - i -1] != reversed_table[str[i]]) {
                        is_mirror = false;
                    }
                } else {
                    is_mirror = false;
                }
            }

            if (!is_mirror && !is_palindromes) {
                break;
            }
        }

        if (is_mirror && is_palindromes) {
            cout << str << " -- is a mirrored palindrome.\n\n";
        } else if (!is_mirror && is_palindromes) {
            cout << str << " -- is a regular palindrome.\n\n";
        } else if (is_mirror && !is_palindromes) {
            cout << str << " -- is a mirrored string.\n\n";
        } else {
            cout << str << " -- is not a palindrome.\n\n";
        }
    }

    return 0;
}