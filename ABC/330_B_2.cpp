#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, L, R;
  cin >> N >> L >> R;
  vector<int> A(N);
  for (int i = 0; i < N; i++)
    cin >> A[i];
  for (int i = 0; i < N; i++)
  {
    cout << clamp(A[i], L, R); // L未満 → L, R以上→R, L以上R未満→A[i] を返す
    if (i == N - 1)
      cout << endl;
    else
      cout << " ";
  }
}