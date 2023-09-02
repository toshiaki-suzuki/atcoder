N = int(input())

f = [[0 for _ in range(100)] for _ in range(100)]

s = 0
for i in range(N):
    A, B, C, D = map(int, input().split())
    for j in range(A, B):
        for k in range(C, D):
            if f[j][k] == 0:
                f[j][k] += 1
                s += 1
print(s)
