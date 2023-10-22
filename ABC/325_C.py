# 各方向を表す配列。上下左右および斜めの8方向を示しています。
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]


def main():
    # 入力を受け取る
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    ans = 0
    # 訪問済みかどうかをチェックするための二次元リスト
    used = [[False] * w for _ in range(h)]

    # 各セルを順番に見ていく
    for i in range(h):
        for j in range(w):
            # '.'はセンサがないセルを表し、すでに訪問済みのセルはスキップする
            if s[i][j] == '.' or used[i][j]:
                continue

            # BFSのためのキューを初期化
            que = [(i, j)]

            # BFSの処理開始
            while que:
                x, y = que.pop(0)
                for d in range(8):  # 8方向を調べる
                    nx, ny = x + dx[d], y + dy[d]
                    # マップの範囲内か、センサがあるセルか、未訪問のセルかを確認
                    if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == '#' and not used[nx][ny]:
                        used[nx][ny] = True
                        que.append((nx, ny))

            # 連結成分を1つ発見したため、答えをインクリメント
            ans += 1

    # 答えを出力
    print(ans)


if __name__ == "__main__":
    main()
