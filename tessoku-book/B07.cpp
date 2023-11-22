#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int T,N;
  cin >> T >> N;
  vector<int> L(500001);
  vector<int> R(500001);
  for (int i = 0; i < N; i++) cin >> L[i] >> R[i];
  
  // 人の増減のを記録
  vector<int> S(500001);
  for (int i = 0; i < N; i++) {
    S[L[i]]++;
    S[R[i]]--;
  }
  
  // 累積和
  for (int i = 1; i <= T; i++) {
      S[i] += S[i - 1];
  }
  
  for (int i = 0; i < T; i++) {
      cout << S[i] << endl;
  }
}