#include <iostream>
using namespace std;

int N, X, A[100009];

// 整数 x が何番目に存在するかを返す
int search(int x)
{
  int L = 1, R = N;
  while (L <= R)
  {                      // 探索範囲がなくなるまで、比較を続ける
    int M = (L + R) / 2; // 中間を導出
    if (x < A[M])
      R = M - 1; // 中間より小さい場合、右辺を中間点の左隣に移動
    if (x == A[M])
      return M; // 発見したら返す
    if (x > A[M])
      L = M + 1; // 中間より大きい場合、左辺を中間点の右隣に移動
  }
  return -1; // 整数 x が存在しない場合（注：この問題の制約で -1 が返されることはない）
}

int main()
{
  // 入力
  cin >> N >> X;
  for (int i = 1; i <= N; i++)
    cin >> A[i];

  // 二分探索を行う
  int Answer = search(X);
  cout << Answer << endl;
  return 0;
}