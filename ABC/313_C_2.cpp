#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  cin >> n;         // 数列の長さ N を入力
  vector<int> a(n); // 数列 A のためのベクターを宣言
  for (int i = 0; i < n; i++)
    cin >> a[i]; // 数列 A の要素を入力

  // 数値ごとにその数値が現れるインデックスを格納するマップ d を作成
  map<int, vector<int>> d;
  for (int i = 0; i < n; i++)
    d[a[i]].push_back(i);

  // 数列 A の合計値 s を計算
  long long s = accumulate(a.begin(), a.end(), 0LL); // 0LL は 0 の long long 型を初期値として指定するためのもの

  // 各要素について、それより大きい要素の和を格納するベクター ans を宣言
  vector<long long> ans(n);
  // d を走査し、各数値 v に対して v より大きい要素の和を計算
  for (auto [v, i_list] : d)
  {
    s -= (long long)v * i_list.size(); // v と等しい要素を合計値 s から引く
    for (auto i : i_list)              // autoは型推論
      ans[i] = s;                      // ans[i] に v より大きい要素の和を格納
  }

  // 答えを出力
  for (auto x : ans)
    cout << x << ' ';
}
