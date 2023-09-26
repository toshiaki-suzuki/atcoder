# すべての321-like Numberを生成する
ans = []
# 10桁の場合の数分だけループさせる
for i in range(2, 1 << 10):  # 1<<10は2の10乗、1024。rangeは2から1023までの数を生成します。
    x = 0
    for j in range(9, -1, -1):  # 9から0まで逆順でループします。
        if i & (1 << j):  # もしiのビット表現でjビット目が1なら
            x *= 10
            x += j  # xにjを追加します。
    ans.append(x)  # xを答えのリストに追加します。

# 結果のリストをソートします。
ans.sort()

# 入力を受け取ります。
k = int(input().strip())

# k番目の321-like Numberを出力します。
print(ans[k - 1])
