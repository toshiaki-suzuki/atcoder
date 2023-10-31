N, D = map(int, input().split())
S = [input() for _ in range(N)]

count = 0
ans = 0
for i in range(D):
    free = True
    for j in range(N):
        if S[j][i] == "x":
            free = False
    if free:
        count += 1
    else:
        count = 0
    ans = max(ans, count)
print(ans)
