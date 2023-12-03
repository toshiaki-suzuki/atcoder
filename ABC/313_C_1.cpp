#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N;
  cin >> N;
  vector<int> A(N);
  vector<long long> S(1000001, 0), T(1000001, 0);

  // 数列 A の読み込みと、各要素の合計値の計算
  for (int i = 0; i < N; i++)
  {
    cin >> A[i];
    S[A[i]] += A[i];
  }

  // 累積和の計算
  for (int i = 1; i <= 1000000; i++)
  {
    T[i] = T[i - 1] + S[i];
  }

  // 各 A[i] に対して、それより大きい要素の合計を計算
  for (int i = 0; i < N; i++)
  {
    cout << T[1000000] - T[A[i]];
    if (i < N - 1)
    {
      cout << " ";
    }
  }
  cout << endl;

  return 0;
}
