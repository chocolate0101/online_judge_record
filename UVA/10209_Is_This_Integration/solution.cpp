#include <bits/stdc++.h>
using namespace std;

int main() {
    double radius;
    while (cin >> radius) {
        double striped_region = radius * radius * (M_PI / 3 - sqrt(3) + 1);
        double dotted_region = 2 * radius * radius * (M_PI / 6 + sqrt(3) - 2);
        double rest_region = 4 * radius * radius * (1 - M_PI / 6 - sqrt(3) / 4);

        cout << fixed << setprecision(3);
        cout << striped_region << " " << dotted_region << " " << rest_region << endl;
    }

    return 0;
}