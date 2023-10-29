# プレゼントの個数Nと半開区間の長さMを入力として受け取る
N, M = map(int, input().split())
# プレゼントの座標をスペースで区切られた形式で入力として受け取り、その後でソートする
A = sorted(list(map(int, input().split())))

# 最大のプレゼントの個数を保持する変数を初期化
ans = 0
# rightポインタを初期化。これは尺取り法の右側の端を示す。
right = 0

# leftポインタ（尺取り法の左側の端）を0からN-1まで移動させる
for left in range(N):
    # rightポインタを進めることができる（プレゼントの範囲内）場合、かつ、
    # 次のプレゼントが半開区間 [A[left], A[left] + M) の範囲内である場合、rightポインタを進める
    while right < N and A[right] < A[left] + M:
        right += 1
    # 現在のleftとrightの位置でのプレゼントの数（right - left）を計算し、これまでの最大値と比較して更新
    ans = max(ans, right - left)

# 最大のプレゼントの個数を出力
print(ans)
