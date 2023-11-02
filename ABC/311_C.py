N = int(input())
A = list(map(int, input().split()))
A.insert(0, -1)  # 1-indexedのためのダミーの値

visited = [False] * (N + 1)
ns = []
v = 1

# 全ての訪れた頂点を追加しながら、閉路の開始頂点を探す
while not visited[v]:
    visited[v] = True
    ns.append(v)
    v = A[v]

# 閉路の開始頂点以降の頂点のみを結果として出力
start_cycling = False
res = []

for n in ns:
    if v == n:  # 閉路の開始頂点を検出
        start_cycling = True
    if start_cycling:
        res.append(n)

print(len(res))
print(*res)
