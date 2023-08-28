M = int(input())
D = list(map(int, input().split()))

mid = (sum(D) + 1) // 2
acc = 0

m = 0
d = 0

for i in range(M):
    acc += D[i]
    if acc >= mid:
        m = i + 1
        d = mid - (acc - D[i])
        break
print(m, d)
