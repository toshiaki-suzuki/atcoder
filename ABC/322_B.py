N, M = map(int, input().split())
S = input()
T = input()

head = ""
tail = ""
for i in range(N):
    head += T[i]
for i in range(1, N + 1):
    tail += T[-i]
tail = tail[::-1]


ans = 3
if S == head and S == tail:
    ans = 0
elif S == head:
    ans = 1
elif S == tail:
    ans = 2

print(ans)
