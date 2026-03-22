#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_map<char, char> mapping_table = {
        {'W', 'Q'}, {'E', 'W'}, {'R', 'E'}, {'T', 'R'}, {'Y', 'T'},
        {'U', 'Y'}, {'I', 'U'}, {'O', 'I'}, {'P', 'O'}, {'[', 'P'},
        {'S', 'A'}, {'D', 'S'}, {'F', 'D'}, {'G', 'F'}, {'H', 'G'},
        {'J', 'H'}, {'K', 'J'}, {'L', 'K'}, {';', 'L'}, {'X', 'Z'},
        {'C', 'X'}, {'V', 'C'}, {'B', 'V'}, {'N', 'B'}, {'M', 'N'},
        {',', 'M'}, {'2', '1'}, {'3', '2'}, {'4', '3'}, {'5', '4'},
        {'6', '5'}, {'7', '6'}, {'8', '7'}, {'9', '8'}, {'0', '9'},
        {'-', '0'}, {'=', '-'}, {']', '['}, {'/', '.'}, {'\\', ']'},
        {'1', '`'}, {'\'', ';'}, {'.', ','}
    };

    string str;
    vector<string> output;
    while (getline(cin, str)) {
        string tmp = "";
        for (auto& ch: str) {
            if (ch == ' ') {
                tmp += ch;
            } else {
                tmp += mapping_table[ch];
            }
        }

        output.push_back(tmp);
    }

    int size = output.size();
    for (int i = 0; i < size; i++) {
        cout << output[i] << endl;
    }

    return 0;
}