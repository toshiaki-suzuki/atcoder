N, X = map(int, input().split())
S = list(map(int, input().split()))

S.sort()
mx = S[-1]
mn = S[0]

ans = -1
for i in range(101):
    sum = 0
    if i <= mn:
        for j in range(0, N-2):
            sum += S[j]
    elif i >= mx:
        for j in range(1, N-1):
            sum += S[j]
    else:
        for j in range(1, N-2):
            sum += S[j]
        sum += i
    if sum >= X:
        ans = i
        break

print(ans)
