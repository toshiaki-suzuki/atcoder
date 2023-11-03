N, M = map(int, input().split())

goods = []
for i in range(N):
    G = list(map(int, input().split()))
    P = G[0]
    C = G[1]
    F = G[2:]
    goods.append([P, C, F])


ans = "No"
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if goods[i][0] >= goods[j][0]:
            if set(goods[i][2]) <= set(goods[j][2]):
                if goods[i][0] > goods[j][0] or set(
                        goods[i][2]) < set(goods[j][2]):
                    ans = "Yes"
                    break
print(ans)
