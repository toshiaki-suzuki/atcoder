# キーワード: 貪欲法, 累積和

n, d, p = map(int, input().split())

f = list(map(int, input().split()))

# fをソート
f.sort()

# 累積和sを計算
s = [0] * n
s[0] = f[0]
for i in range(1, n):
    s[i] = s[i-1] + f[i]

# 最大で必要な1日周遊パスのセット数を計算
k = (n + d - 1) // d

# すべての日に1日周遊パスを利用する場合のコストで初期化
ans = p * k

# 最も高い日からd日ずつ1日周遊パスを利用しない場合のコストを計算し、最小のコストを更新
for i in range(k):
    ans = min(ans, s[n - 1 - (i * d)] + (p * i))

print(ans)
