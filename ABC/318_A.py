N, M, P = map(int, input().split())

cnt = 0
d = M
while d <= N:
    d += P
    cnt += 1
print(cnt)
