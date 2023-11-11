N = int(input())
D = list(map(int, input().split()))
D.insert(0, -1)

ans = 0
for i in range(1, N+1):
    str_i = str(i)
    for j in range(1, D[i]+1):
        day = str_i + str(j)
        flg = True
        digit = day[0]
        for d in day:
            if d != digit:
                flg = False
        if flg:
            ans += 1

print(ans)
