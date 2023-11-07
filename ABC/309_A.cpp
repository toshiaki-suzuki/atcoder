#include <bits/stdc++.h>
using namespace std;

int main() {
  int A,B;
  cin >> A >> B;
  string ans = "No";
  if (A == B + 1 && B % 3 != 0) {
    ans = "Yes";
  }
  if (A == B - 1 && B % 3 != 1) {
    ans = "Yes";
  }
  cout << ans << endl;
}