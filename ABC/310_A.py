N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

prices = [P]
for i in range(N):
    prices.append(Q + D[i])
print(min(prices))
