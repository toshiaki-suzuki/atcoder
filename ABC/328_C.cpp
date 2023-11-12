#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    char s[300001];
    int a[300000] = {0}, b[300000] = {0};

    for (int i = 0; i < n; i++) {
        cin >> s[i];
    }

    for (int i = 0; i < n - 1; i++) {
        if (s[i] == s[i + 1]) {
            a[i] = 1;
        }
    }

    for (int i = 1; i < n; i++) {
        b[i] = b[i - 1] + a[i - 1];
    }

    int l, r;
    for (int i = 0; i < q; i++) {
        cin >> l >> r;
        cout << b[r - 1] - b[l - 1] << "\n";
    }
}
