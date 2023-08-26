N, H, X = map(int, input().split())
P = list(map(int, input().split()))

for i in range(1, N+1):
    hp = H + P[i]
    if hp > X:
        print(i)
        break
