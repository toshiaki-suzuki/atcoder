N = int(input())
S = input()

ans = -1
for i in range(N):
    if S[i] == "A" and i < N - 2:
        if S[i + 1] == "B":
            if S[i + 2] == "C":
                ans = i + 1
                break
print(ans)
