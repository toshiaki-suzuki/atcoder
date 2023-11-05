# 標準入力から棒の本数Nを読み込む
N = int(input())

# 各棒についての文字列を格納するリストを作成
S = [input() for _ in range(N)]

# すべての異なる棒を保持するためのセット
unique_rods = set()

# 各棒に対してループを行う
for rod in S:
    # 現在の棒の逆文字列を作成
    reversed_rod = rod[::-1]

    # 並べ替えられたタプルとして、棒とその逆文字列をセットに追加
    # これにより、棒がどちらの向きでも同じように扱われる
    unique_rods.add(tuple(sorted([rod, reversed_rod])))

# セット内の異なる要素の数（異なる棒の種類の数）を出力
print(len(unique_rods))
