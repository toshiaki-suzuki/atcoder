#include <bits/stdc++.h>
using namespace std;

int H, W, N;              // 縦 (H) 、横 (W)、日数 (N)
int A[100009], B[100009]; // 各日の左上の座標 (A[t], B[t])
int C[100009], D[100009]; // 各日の右下の座標 (C[t], D[t])
int X[1509][1509];        // 差分配列
int Z[1509][1509];        // 最終的な積雪量の累積和

int main()
{
  // 入力を受け取る
  cin >> H >> W >> N;
  for (int t = 1; t <= N; t++)
    cin >> A[t] >> B[t] >> C[t] >> D[t];

  // 差分配列を使用して積雪の増加を記録
  for (int t = 1; t <= N; t++)
  {
    X[A[t]][B[t]] += 1;
    X[A[t]][D[t] + 1] -= 1;
    X[C[t] + 1][B[t]] -= 1;
    X[C[t] + 1][D[t] + 1] += 1;
  }

  // 初期化（全マスを0に設定）
  for (int i = 0; i <= H; i++)
  {
    for (int j = 0; j <= W; j++)
      Z[i][j] = 0;
  }

  // 横方向の累積和を計算
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
      Z[i][j] = Z[i][j - 1] + X[i][j];
  }

  // 縦方向の累積和を計算
  for (int j = 1; j <= W; j++)
  {
    for (int i = 1; i <= H; i++)
      Z[i][j] = Z[i - 1][j] + Z[i][j];
  }

  // 最終的な積雪量を出力
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
    {
      if (j >= 2)
        cout << " "; // スペースで区切って出力
      cout << Z[i][j];
    }
    cout << endl;
  }
  return 0;
}
