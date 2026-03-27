#include <bits/stdc++.h>
using namespace std;

int main() {
    long long cases;
    cin >> cases;
    string line;
    getline(cin, line);
    getline(cin, line);

    for (long long i = 0; i < cases; i++) {
        map<string, double> species;
        string tree_name;
        double total_species = 0;
        while (1) {
            getline(cin, tree_name);
            if (tree_name != "") {
                species[tree_name]++;
                total_species++;
            } else {
                break;
            }
        }

        for (auto& it: species) {
            cout << fixed << setprecision(4);
            cout << it.first << " " << it.second * (double)100 / total_species << endl;
        }

        if (i != cases - 1) {
            cout << endl;
        }
    }

    return 0;
}