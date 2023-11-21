#include <iostream>
using namespace std;

int N, A[100009];
int Q, L[100009], R[100009];
int Atari[100009], Hazre[100009];

int main()
{
  // 入力
  cin >> N;
  for (int i = 1; i <= N; i++)
    cin >> A[i]; // 投票結果を入力
  cin >> Q;
  for (int i = 1; i <= Q; i++)
    cin >> L[i] >> R[i]; // 左端と右端の値を格納

  // アタリの個数・ハズレの個数の累積和を求める
  Atari[0] = 0;
  Hazre[0] = 0;
  for (int i = 1; i <= N; i++)
  {
    Atari[i] = Atari[i - 1]; // 前の投票の値を代入
    if (A[i] == 1)
      Atari[i] += 1; // アタリだったら累積和を増やす

    Hazre[i] = Hazre[i - 1]; // 前の投票の値を代入
    if (A[i] == 0)
      Hazre[i] += 1; // 流行りだったら累積和を増やす
  }

  // 質問に答える
  for (int i = 1; i <= Q; i++)
  {
    // 範囲内の累積和を求める
    int NumAtari = Atari[R[i]] - Atari[L[i] - 1];
    int NumHazre = Hazre[R[i]] - Hazre[L[i] - 1];

    if (NumAtari > NumHazre)
      cout << "win" << endl;
    else if (NumAtari == NumHazre)
      cout << "draw" << endl;
    else
      cout << "lose" << endl;
  }
  return 0;
}