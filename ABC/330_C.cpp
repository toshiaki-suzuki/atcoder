#include <iostream>
#include <cmath>
#include <limits>

using namespace std;

int main()
{
  long long D;
  cin >> D; // 標準入力からDを読み込む

  // 最小差分を格納する変数。初期値はlong longの最大値に設定
  long long minDiff = numeric_limits<long long>::max(); // long long は 64bit 整数型
  // 最適なx、yの値を格納する変数
  long long x_best = 0, y_best = 0;

  // xの値を0からsqrt(D)まで繰り返す
  for (long long x = 0; x * x <= D; ++x)
  {
    // yの値を計算する。ここではDからx^2を引いた値の平方根を丸める
    long long y = round(sqrt(D - x * x));
    // 現在のx、yの組み合わせにおける差分を計算
    long long diff = abs(x * x + y * y - D);
    // これまでの最小差分よりも小さい場合は、最小差分とx、yの値を更新
    if (diff < minDiff)
    {
      minDiff = diff;
      x_best = x;
      y_best = y;
    }
  }

  // 最小差分を出力
  cout << minDiff << endl;

  return 0;
}
