#include <bits/stdc++.h>
using namespace std;

int N; 
int A[100009]; // Aの配列
int S[100009]; // 累積和の配列
int Q;
int L[100009]; 
int R[100009]; 

int main() {
  cin >> N >> Q;
  
  for (int i=1; i<=N; i++) cin >> A[i];
  for (int j=1; j<=Q; j++) cin >> L[j] >> R[j];
  
  S[0] = 0;
  for(int i; i<=N; i++) S[i] = S[i-1] + A[i]; // 前日の累積和に今日の来場者数を足す
  
  for(int j=1; j<=Q; j++) {
    cout << S[R[j]] - S[L[j]-1] << endl;
  }
  return 0;
}
