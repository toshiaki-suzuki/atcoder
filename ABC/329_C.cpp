#include <bits/stdc++.h>

using namespace std;

int main()
{
  int N;
  string S;
  cin >> N >> S;

  // 文字の種類を入れる配列
  vector<int> mx(26);

  // 各文字が連続で続く最長の文字数を求める
  int l = 0;
  while (l < N)
  {
    int r = l + 1;
    while (r < N and S[l] == S[r])
      r++;
    int c = S[l] - 'a';        // ASCII codeに変換してaのASCII codeを引くと、何番目の文字かがわかる
    mx[c] = max(mx[c], r - l); // その文字の最長部分文字列の長さを更新
    l = r;
  }

  int ans = 0;
  for (int i = 0; i < 26; i++)
  {
    ans += mx[i];
  }
  cout << ans << endl;
}
