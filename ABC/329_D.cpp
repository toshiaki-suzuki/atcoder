#include <bits/stdc++.h>
using namespace std;

int main()
{
  int N, M;
  cin >> N >> M;
  vector<int> A(M);
  for (int i = 0; i < M; i++)
    cin >> A[i]; // 各投票結果

  vector<int> cnt(N + 1); // 各候補者の投票数

  int ans = 0; // 初期化時点の当選者
  for (int i = 0; i < M; i++)
  {
    cnt[A[i]]++;
    if (cnt[A[i]] > cnt[ans])
      ans = A[i];
    else if (cnt[A[i]] == cnt[ans])
      ans = min(ans, A[i]);
    cout << ans << endl;
  }
}