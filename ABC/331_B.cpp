#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, S, M, L;
  cin >> N >> S >> M >> L;

  vector<int> price_list;

  int ans = 9999999;
  for (int i = 0; i <= N; i++)
  {
    for (int j = 0; j <= N; j++)
    {
      for (int k = 0; k <= N; k++)
      {
        if (6 * i + 8 * j + 12 * k >= N)
          ans = min(ans, S * i + M * j + L * k);
      }
    }
  }
  cout << ans << endl;
}