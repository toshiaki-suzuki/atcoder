N = int(input())

yaku = []
for i in range(1, N+1):
    if N % i == 0 and i <= 9:
        yaku.append(i)

ans = ''
for i in range(N+1):
    for j in yaku:
        s = '-'
        if i % (N//j) == 0:
            s = str(j)
            break
    ans += s

print(ans)
