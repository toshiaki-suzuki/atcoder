#include <bits/stdc++.h>
using namespace std;

int H, W, Q;              // 縦、横、質問数
int X[1509][1509];              // 各座標の値
int Z[1509][1509];              // 累積和
int A[100009], B[100009]; // 左上の座標
int C[100009], D[100009]; // 右下の座標

int main()
{
  cin >> H >> W;
  // 座標に値を格納
  for (int i=1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
      cin >> X[i][j];
  }
  cin >> Q;
  // 各質問の座標を入力
  for (int i=1; i <= Q; i++)
    cin >> A[i] >> B[i] >> C[i] >> D[i];

  // 配列Z(累積和)の初期化
  for (int i = 0; i <= H; i++)
  {
    for (int j = 0; j <= W; j++)
      Z[i][j] = 0;
  }

  // 横方向の累積和
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
      Z[i][j] = Z[i][j - 1] + X[i][j];
  }

  // 縦方向の累積和
  for (int i = 1; i <= H; i++)
  {
    for (int j = 1; j <= W; j++)
      Z[i][j] = Z[i - 1][j] + Z[i][j];
  }

  // 答えを求める
  for (int i = 1; i <= Q; i++)
  {
    cout << Z[C[i]][D[i]] + Z[A[i] - 1][B[i] - 1] - Z[A[i] - 1][D[i]] - Z[C[i]][B[i]-1] << endl;
  }
  return 0;
}