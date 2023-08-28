def strongest_programmer():
    N, M = map(int, input().split())

    # 入度 (入ってくるエッジの数) を保存するリスト
    # 0 で初期化された N 要素のリストを作成
    deg = [0] * N

    # 与えられた関係性をもとに、各ノードの入度を計算
    for _ in range(M):
        a, b = map(int, input().split())
        # 0-indexed に変換するために 1 を減算
        a -= 1
        b -= 1
        deg[b] += 1  # b に入ってくるエッジの数を増やす

    ans = -1  # 最初は答えを -1 としておく

    # 全てのノードに対して、入度が 0 のものを探す
    # 入度が 0 のノードは他のノードからエッジが来ていないことを意味する
    for i in range(N):
        if deg[i] == 0:
            # すでに入度が 0 のノードが見つかっていた場合、答えは -1 となる
            if ans != -1:
                return -1  # 2つ以上のノードが入度 0 の場合、答えは -1 となる
            else:
                ans = i + 1  # 0-indexed から 1-indexed に戻す

    return ans  # 最強のプログラマーの番号を返す、または -1


# 結果を出力
print(strongest_programmer())
