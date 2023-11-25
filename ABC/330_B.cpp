#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, L, R;
  cin >> N >> L >> R;
  int A[N];
  for (int i = 0; i < N; i++)
    cin >> A[i];

  for (int i = 0; i < N; i++)
  {
    int ans = -1;
    if (A[i] >= L and A[i] <= R)
    {
      ans = A[i];
    }
    else
    {
      if (A[i] <= L)
        ans = L;
      else if (A[i] >= R)
        ans = R;
    }
    cout << ans;
    if (i != N - 1)
      cout << " ";
  }
}