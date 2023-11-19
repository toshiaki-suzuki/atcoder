#include <bits/stdc++.h>
using namespace std;


int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  vector<int> newA(N);
  
  for(int i=0; i<N; i++) cin >> A[i];
  int mx = *max_element(A.begin(), A.end());
  
  int ans = 0;
  for(int i=0; i<N; i++) {
    if(mx == A.at(i)) continue;
    ans = max(A.at(i), ans);
  }
  
  cout << ans << endl;
}