#include <bits/stdc++.h>
using namespace std;

int N[100009], X[100009], Y[100009];
int Q, A[100009], B[100009], C[100009], D[100009];

int S[1509][1509];
int T[1509][1509];

int main()
{
  cin >> N; // 座標の数
  for (int i = 1; i <= N; i++)
    cin >> X[i] >> Y[i]; // 座標を入力
  cin >> Q;              // 質問の数
  for (int i = 1; i <= Q; i++)
    cin >> A[i] >> B[i] >> C[i] >> D[i]; // 質問の座標を入力

  for (int i = 1; i <= N; i++)
    S[X[i]][Y[i]] += 1; // 各座標の点を数を数える

  // 累積和の配列を初期化
  for (int i = 0; i <= 1500; i++)
  {
    for (int j = 0; j <= 1500; j++)
      T[i][j] = 0;
  }

  // 水平方向の累積和を計算
  for (int i = 0; i <= 1500; i++)
  {
    for (int j = 1; j <= 1500; j++)
      T[i][j] = T[i][j - 1] + S[i][j]; // 現在の1つ左の座標 + 座標
  }

  // 垂直方向に累積和を計算
  for (int i = 1; i <= 1500; i++)
  {
    for (int j = 1; j <= 1500; j++)
      T[i][j] = T[i - 1][j] + T[i][j]; // 現在の1つ上の座標 + 座標
  }

  // 答えを求める
  for (int i = 1; i <= Q; i++)
  {
    cout << T[C[i]][D[i]] + T[A[i] - 1][B[i] - 1] - T[A[i] - 1][D[i]] - T[C[i]][B[i] - 1] << endl;
  }
  return 0;
}